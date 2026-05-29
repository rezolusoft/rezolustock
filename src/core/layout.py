from layout import pager, onboarder

def build_layout(page, result, container):

    if result["type"] == "error":
        return result["content"]
    
    layout_type = result["layout"]
    content = result["content"]

    if layout_type == "auth":
        return content
    
    
    container.content = content
    
    if layout_type == "main":
        return pager(page=page, content=container)
    
    if layout_type == "onboarding":
        return onboarder(content=content, illustration=page.route.lstrip("/"))
    
    