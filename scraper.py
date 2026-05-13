import json
from playwright.sync_api import sync_playwright

def scrape_entertainment_news(page):

    print("Navigating to entertainment...")
    page.goto("https://ekantipur.com/entertainment")

    #Wait for the article cards to load
    page.wait_for_selector(".category", timeout=15000)

    #scroll down so lazy laoding images are triggered
    page.evaluate("window.scrollTo(0,800)")
    page.wait_for_timeout(2000)

    articles = []
    seen_titles = set() # Tracking titles to avoid duplis

    cards = page.query_selector_all(".category")
    print(f"Found {len(cards)} articles in total. Scraping top 5 articles...")

    for card in cards:
        if len(articles) == 5:
            break

        # TITLE
        title_el = card.query_selector(".category-description h2 a")
        title = title_el.text_content().strip() if title_el else None

        #skip if there are no titles or if its already seen
        if not title or title in seen_titles:
            continue
        seen_titles.add(title)

        # AUTHOR
        author_el = card.query_selector(".author-name p a")
        author = author_el.text_content().strip() if author_el else None

        # IMAGE
        image_el = card.query_selector(".category-image img")
        image_url = image_el.get_attribute("src") if image_el else None

        # CATEGORY
        category_el = card.query_selector(".category-name p a")
        category = category_el.text_content().strip() if category_el else "मनोरञ्जन"

        articles.append({
            "title": title,
            "image_url": image_url,
            "category": category,
            "author": author,
        })

        print(f"{title[:60]}")

    return articles

def scrape_cartoon_of_the_day(page):
    
    print("\nNavigateing to cartoon of the day...")
    page.goto("https://ekantipur.com/cartoon")
    page.wait_for_load_state("networkidle",timeout=15000)
    page.wait_for_timeout(2000)

    #Used different selector beacuse they differ in homepage and category page
    cartoon = page.query_selector(".cartoon-wrapper")

    if not cartoon:
        print(" WARNING: Could not find cartoon wrapper")
        return{"title": None, "image_url": None, "author": None}

    #Image URL 
    img_el = cartoon.query_selector(".cartoon-image img")
    image_url = img_el.get_attribute("src") if img_el else None

    #TITLE and AUTHOR both in <p> tag
    desc_el = cartoon.query_selector(".cartoon-description p")
    title = None
    author = None

    if desc_el:
        text = desc_el.text_content().strip()
        if " - " in text:
            parts = text.split(" - ",1)
            title = parts[0].strip() if parts[0].strip() else None
            author = parts[1].strip() if len(parts) > 1 and parts[1].strip() else None
        else:
            #striping trailing whitespace
            title = text.rstrip("- ").strip() if text else None

    print(f" Cartoon:{title}")
    print(f" Author:{author}")

    return{
        "title":title,
        "image_url":image_url,
        "author":author
    }

def main():
    with sync_playwright() as p:
            
        #headless = false to watch the browser to debug issues visually
        browser = p.chromium.launch(headless=False) 
        page = browser.new_page()

        try:
            #Task1
            entertainment_news = scrape_entertainment_news(page)

            #Task2
            cartoon_of_the_day = scrape_cartoon_of_the_day(page)

            output = {
                "entertainment_news":entertainment_news,
                "cartoon_of_the_day":cartoon_of_the_day
            }

            #Saving to output.json/ ensure_ascii = false to preserve nepali text
            with open("output.json","w", encoding="utf-8") as f:
                json.dump(output, f, ensure_ascii=False, indent=2)

            print("\n Done! Saved to output.json")
            print("\n--- Preview ---")
            print(json.dumps(output, ensure_ascii = False, indent=2))
            

        except Exception as e:
            print(f"\n Script Failed: {e}")
            raise

        finally:
            browser.close()


if __name__ == "__main__":
    main()