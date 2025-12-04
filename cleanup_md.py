import os
import re

DOCS_DIR = 'docs'

def cleanup_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove the anchor links like [¶](#...)
    # Pattern matches [¶] followed by (...)
    # The regex handles the link part which might contain quotes
    content = re.sub(r'\[¶\]\(.*?\)', '', content)

    # 2. Remove the "Discussion" section and Disqus footer
    # We look for "## 讨论" and remove it and everything that follows, 
    # OR specific Disqus lines if the header is missing.
    
    # Strategy: Split by lines and filter
    lines = content.splitlines()
    new_lines = []
    skip = False
    
    for line in lines:
        # Check for Discussion header
        if line.strip().startswith('## 讨论'):
            skip = True # Assuming Discussion is at the end
            continue
            
        if skip:
            # We can check if we hit another header, but usually Discussion is the last section for these docs.
            # However, to be safe, if we encounter another header (that isn't a sub-header of discussion), maybe we should stop skipping?
            # But based on the file viewed, it's at the end.
            # Also check for the specific Disqus text to confirm we are in the trash zone
            pass
        else:
            # Also remove standalone Disqus lines if they exist outside the header block (just in case)
            if 'comments powered by Disqus' in line:
                continue
            new_lines.append(line)
            
    # Reconstruct content
    new_content = '\n'.join(new_lines)
    
    # Remove trailing newlines
    new_content = new_content.strip() + '\n'

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    count = 0
    for root, dirs, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                # print(f"Cleaning {file_path}...")
                cleanup_file(file_path)
                count += 1
    print(f"Cleaned {count} files.")

if __name__ == "__main__":
    main()
