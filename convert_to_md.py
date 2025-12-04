import os
import bs4
from markdownify import markdownify as md

SOURCE_DIR = 'redis-doc'
TARGET_DIR = '_markdown'

def convert_html_to_md(html_content):
    soup = bs4.BeautifulSoup(html_content, 'html.parser')
    
    # Try to find the main article body
    article_body = soup.find(itemprop="articleBody")
    if article_body:
        content_to_convert = str(article_body)
    else:
        # Fallback to body or full content
        body = soup.find('body')
        if body:
            content_to_convert = str(body)
        else:
            content_to_convert = html_content
            
    # Convert to markdown
    # heading_style="ATX" uses # for headers instead of underlining
    return md(content_to_convert, heading_style="ATX")

def main():
    # Create target directory if it doesn't exist
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
        
    # Walk through the source directory
    for root, dirs, files in os.walk(SOURCE_DIR):
        for file in files:
            if file.endswith('.html'):
                source_path = os.path.join(root, file)
                
                # Calculate relative path to maintain structure
                rel_path = os.path.relpath(root, SOURCE_DIR)
                
                # Determine target directory
                if rel_path == '.':
                    target_subdir = TARGET_DIR
                else:
                    target_subdir = os.path.join(TARGET_DIR, rel_path)
                
                if not os.path.exists(target_subdir):
                    os.makedirs(target_subdir)
                
                # Determine target file path
                target_filename = os.path.splitext(file)[0] + '.md'
                target_path = os.path.join(target_subdir, target_filename)
                
                print(f"Converting {source_path} -> {target_path}")
                
                try:
                    with open(source_path, 'r', encoding='utf-8') as f:
                        html_content = f.read()
                        
                    markdown_content = convert_html_to_md(html_content)
                    
                    with open(target_path, 'w', encoding='utf-8') as f:
                        f.write(markdown_content)
                        
                except Exception as e:
                    print(f"Error converting {source_path}: {e}")

if __name__ == "__main__":
    main()
