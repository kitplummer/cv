#!/usr/bin/env python3
"""Apply modern CSS to the generated resume HTML"""

import sys
import re

def apply_modern_css(html_file='kp-resume.html', css_file='resume-modern.css'):
    try:
        # Read the HTML file
        with open(html_file, 'r') as f:
            html_content = f.read()
        
        # Read the CSS file
        with open(css_file, 'r') as f:
            css_content = f.read()
        
        # Replace the style section
        # Find and replace everything between <style> tags
        pattern = r'<style type="text/css">.*?</style>'
        replacement = f'<style type="text/css">\n{css_content}\n</style>'
        
        html_content = re.sub(pattern, replacement, html_content, flags=re.DOTALL)
        
        # Fix the mailto link
        html_content = html_content.replace(
            '<a href="kitplummer@gmail.com">kitplummer@gmail.com</a>',
            '<a href="mailto:kitplummer@gmail.com">kitplummer@gmail.com</a>'
        )
        
        # Write the updated HTML
        with open(html_file, 'w') as f:
            f.write(html_content)
        
        print(f"✓ Modern CSS applied to {html_file}")
        return True
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        apply_modern_css(sys.argv[1])
    else:
        apply_modern_css()