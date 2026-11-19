# Python simulation of the HTML structure used in a WordPress post
post_title = "Welcome to My AI Lab Blog"
post_body = "This post explains Artificial Intelligence practical experiments."
html = f"""<article>
  <h1>{post_title}</h1>
  <p>{post_body}</p>
  <a href="https://wordpress.com/">Visit WordPress</a>
</article>"""
print("Generated blog post HTML:")
print(html)
print("\nPaste the title and content into WordPress Posts > Add New to publish.")
