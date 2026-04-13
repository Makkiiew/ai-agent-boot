import os

def get_files_info(working_directory, directory="."):
    try:
        working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir, directory))
        
        if os.path.commonpath([working_dir, target_dir]) != working_dir:
            return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"
        
        if not os.path.isdir(target_dir):
            return f"Error: '{directory}' is not a directory"
        
        items = os.listdir(target_dir)
        output_lines = []

        for name in items:
            item_path = os.path.join(target_dir, name)
            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            output_lines.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")
            
        return "\n".join(output_lines)
        
    except Exception as e:
        return f"Error: {e}"