import os
import json

def search_in_lua_files(root_folder, search_word):
    matches = []
    
    for folder, _, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".lua"):
                file_path = os.path.join(folder, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        for line_number, line in enumerate(lines, start=1):
                            if search_word in line:
                                matches.append({
                                    "file": file_path,
                                    "line": line_number,
                                    "original_content": line.strip(),
                                    "modified_content": line.strip().replace(search_word, "")
                                })
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    
    return matches

def replace_word_in_files(results, old_word, new_word):
    backup_results = []
    
    for match in results:
        file_path = match["file"]
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            modified_lines = []
            for line in lines:
                modified_lines.append(line.replace(old_word, new_word))
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(modified_lines)
            
            backup_results.append({
                "file": file_path,
                "line": match["line"],
                "original_content": match["original_content"],
                "modified_content": match["original_content"].replace(old_word, new_word)
            })
        except Exception as e:
            print(f"Error on update {file_path}: {e}")
    
    return backup_results

def restore_backup(backup_filename):
    try:
        with open(backup_filename, "r", encoding="utf-8") as json_file:
            backup_results = json.load(json_file)
        
        for match in backup_results:
            file_path = match["file"]
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                
                modified_lines = []
                for line in lines:
                    modified_lines.append(line.replace(match["modified_content"], match["original_content"]))
                
                with open(file_path, "w", encoding="utf-8") as f:
                    f.writelines(modified_lines)
                
                print(f"Restored: {file_path}, Linha: {match['line']}")
            except Exception as e:
                print(f"Erro ao restaurar {file_path}: {e}")
    except Exception as e:
        print(f"Erro ao carregar backup: {e}")


if __name__ == "__main__":
    mode = input("type 'replace' or 'restore':")
    
    if mode == "replace":
        folder_to_search = input("Enter the path of the folder to be scanned:")
        search_word = "getWaterAmount"
        replace_word = "getLiquidAmount"
        
        results = search_in_lua_files(folder_to_search, search_word)
        
        if results:
            backup_results = replace_word_in_files(results, search_word, replace_word)
            backup_filename = "backup_results.json"
            with open(backup_filename, "w", encoding="utf-8") as json_file:
                json.dump(backup_results, json_file, indent=4, ensure_ascii=False)
            print(f"Backup salvo em {backup_filename}")
    
    elif mode == "restore":
        backup_filename = "backup_results.json"
        restore_backup(backup_filename)
    
    else:
        print("Invalid mode!")
