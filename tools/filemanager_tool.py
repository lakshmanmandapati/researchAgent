"""
Enhanced File Manager Tool - Prevents Truncation
"""
from crewai.tools import BaseTool
import os
from datetime import datetime

class FileManagerTool(BaseTool):
    name: str = "File Manager Tool"
    description: str = "Save complete outputs to files without truncation"
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        os.makedirs("outputs", exist_ok=True)

    def _run(self, content: str, filename: str = None) -> str:
        """Save content with proper encoding and full content preservation"""
        try:
            if not filename:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"proposal_{timestamp}.md"
            
            if not filename.endswith('.md'):
                filename += '.md'
            
            filepath = os.path.join("outputs", filename)
            
            with open(filepath, "w", encoding="utf-8", newline='\n') as f:
                f.write(content)
            
            file_size = os.path.getsize(filepath)
            content_size = len(content.encode('utf-8'))
            
            return f"✅ File saved: {filepath} ({file_size} bytes, content: {content_size} bytes)"
            
        except Exception as e:
            return f"❌ Error saving file: {str(e)}"

file_manager_tool = FileManagerTool()