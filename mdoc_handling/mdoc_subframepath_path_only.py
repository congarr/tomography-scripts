import os

def update_subframe_path(mdoc_path, new_path):
    with open(mdoc_path, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.startswith('SubFramePath'):
            existing_path = line.split('=')[-1].strip().replace('\\', '/')
            _, existing_filename = os.path.split(existing_path)

            new_subframe_path = f'SubFramePath = {os.path.join(new_path, existing_filename)}\n'
            lines[i] = new_subframe_path

    with open(mdoc_path, 'w') as f:
        f.writelines(lines)

def batch_update_paths(folder_path, new_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.mdoc'):
            mdoc_path = os.path.join(folder_path, filename)
            update_subframe_path(mdoc_path, new_path)
            print(f'SubFramePath updated for {filename}')

mdoc_folder = '/data/garrels/csg067/mdocs/20240403_mdocs/stack_mdocs_copy_3'
new_subframe_path = '/data/garrels/csg067/warp/2024-07-11/average'

batch_update_paths(mdoc_folder, new_subframe_path)
