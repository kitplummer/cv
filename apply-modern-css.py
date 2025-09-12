#!/usr/bin/env python3
"""Apply modern CSS to the generated resume HTML"""

import sys
import re

def apply_modern_css(html_file='kp-resume.html', css_file='resume-modern.css', template_file='kp-template.html'):
    try:
        # Read the HTML file to extract resume content
        with open(html_file, 'r') as f:
            html_content = f.read()
        
        # Read the CSS file
        with open(css_file, 'r') as f:
            css_content = f.read()
        
        # Read the template file
        with open(template_file, 'r') as f:
            template_content = f.read()
        
        # Extract just the resume content inside the container
        container_match = re.search(r'<div class="container">(.*?)</div>\s*</body>', html_content, re.DOTALL)
        if container_match:
            body_content = container_match.group(1).strip()
        else:
            raise ValueError("Could not extract resume content from HTML")
        
        # Apply template
        final_html = template_content.replace('{{{style}}}', css_content)
        final_html = final_html.replace('{{{resume}}}', body_content)
        
        # Remove reload section for production
        final_html = re.sub(r'{{#reload}}.*?{{/reload}}', '', final_html, flags=re.DOTALL)
        
        # Fix the mailto link
        final_html = final_html.replace(
            '<a href="kitplummer@gmail.com">kitplummer@gmail.com</a>',
            '<a href="mailto:kitplummer@gmail.com">kitplummer@gmail.com</a>'
        )
        
        # Write the updated HTML
        with open(html_file, 'w') as f:
            f.write(final_html)
        
        print(f"✓ Modern template with dark mode applied to {html_file}")
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