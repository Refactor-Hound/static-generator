import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    # def test_props_to_html_with_single_prop(self):
    #     """Test that a single prop is converted correctly to HTML attributes"""
    #     node = HTMLNode(tag="a", props={"href": "https://www.google.com"})
    #     expected = ' href="https://www.google.com"'
    #     self.assertEqual(node.props_to_html(), expected)
    
    # def test_props_to_html_with_multiple_props(self):
    #     """Test that multiple props are converted correctly to HTML attributes"""
    #     node = HTMLNode(
    #         tag="a",
    #         props={
    #             "href": "https://www.google.com",
    #             "target": "_blank"
    #         }
    #     )
    #     result = node.props_to_html()
    #     # Check that the result starts with a space
    #     self.assertTrue(result.startswith(" "))
    #     # Check that both attributes are present
    #     self.assertIn('href="https://www.google.com"', result)
    #     self.assertIn('target="_blank"', result)
    
    def test_props_to_html_with_no_props(self):
        """Test that an empty props dictionary returns an empty string"""
        node = HTMLNode(tag="p", value="Hello, world!")
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_with_none_props(self):
        """Test that None props returns an empty string"""
        node = HTMLNode(tag="p", value="Hello, world!", props=None)
        self.assertEqual(node.props_to_html(), "")
    
    def test_repr(self):
        """Test that __repr__ returns a useful string representation"""
        node = HTMLNode(
            tag="a",
            value="Click me",
            props={"href": "https://www.example.com"}
        )
        repr_str = repr(node)
        # Check that the repr contains key information
        self.assertIn("HTMLNode", repr_str)
        self.assertIn("tag='a'", repr_str)
        self.assertIn("value='Click me'", repr_str)
        self.assertIn("href", repr_str)
    
    def test_to_html_raises_not_implemented(self):
        """Test that calling to_html raises NotImplementedError"""
        node = HTMLNode(tag="p", value="test")
        with self.assertRaises(NotImplementedError):
            node.to_html()
    
    def test_node_with_children(self):
        """Test that a node can have children"""
        child_node = HTMLNode(tag="span", value="child")
        parent_node = HTMLNode(tag="div", children=[child_node])
        self.assertEqual(len(parent_node.children), 1)
        self.assertEqual(parent_node.children[0].tag, "span")
    
    def test_node_defaults_to_none(self):
        """Test that all parameters default to None"""
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)


if __name__ == "__main__":
    unittest.main()