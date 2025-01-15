from crewai_tools import ScrapeWebsiteTool

class DocumentationScraper(ScrapeWebsiteTool):
    def __init__(self, website_url):
        super().__init__(website_url=website_url)
