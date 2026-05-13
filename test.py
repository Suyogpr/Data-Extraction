# def main():
#     # print("Hello from ekantipur-scraper!")
#     from playwright.sync_api import sync_playwright

#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)  # set True for background mode
#         page = browser.new_page()

#         page.goto("https://ekantipur.com/entertainment")
#         print("page title",page.title())
#         category = page.query_selector(".category-name >  p>  a").text_content()
#         print("category",category)
#         # title = page.query_selector_all(".category-description > h2 > a").text_content()
#         # print("title",title)
#         categories= page.query_selector_all(".category-description")
#         for category in categories:
#             title = category.query_selector("h2 >a").text_content()
#         browser.close()


# if __name__ == "__main__":
#     main()


# def main():
#     from playwright.sync_api import sync_playwright

#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)

#         page = browser.new_page()

        
#         page.goto("https://ekantipur.com/entertainment")

#         categorie = page.query_selector(".category-name>p>a").text_content()

#         categories = page.query_selector_all(".category")

#         for i, category in enumerate(categories[:5], start=1):
#             title = category.query_selector(".category-description >h2>a").text_content()
#             author = category.query_selector(".author-name>p>a").text_content()
#             image = category.query_selector(".category-image>a>figure>img").get_attribute("src")
#             categorie = categorie
#             print(f"{i}. {title} {author} {image} {categorie}")

#         browser.close()


# if __name__ == "__main__":
#     main()

    
