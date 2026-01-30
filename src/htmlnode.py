class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props:
            props_str = ""

            for key, value in self.props.items():
                props_str += f' {key}="{value}"'
            return props_str
        else:
            return ""
    def __repr__(self):
        node = f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        return node

