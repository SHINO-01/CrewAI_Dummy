class StructuredDataQueryTool:
    """
    A custom tool for querying structured data extracted from documentation.
    """

    def __init__(self):
        self.structured_data = None

    def load_data(self, structured_data):
        """
        Load structured data into the tool for querying.
        :param structured_data: List of dictionaries or strings representing the documentation content.
        """
        if not isinstance(structured_data, (list, dict)):
            raise TypeError("Structured data must be a list or dictionary.")
        self.structured_data = structured_data

    def query(self, user_query):
        """
        Query the structured data for relevant information.
        :param user_query: A string representing the user's query.
        :return: A list of matching results from the structured data.
        """
        if self.structured_data is None:
            raise ValueError("No structured data loaded. Please load data before querying.")

        results = []

        # Search through the structured data
        if isinstance(self.structured_data, list):
            for entry in self.structured_data:
                if isinstance(entry, dict):
                    for key, value in entry.items():
                        if user_query.lower() in str(value).lower():
                            results.append({key: value})
                elif isinstance(entry, str):
                    if user_query.lower() in entry.lower():
                        results.append(entry)
        elif isinstance(self.structured_data, dict):
            for key, value in self.structured_data.items():
                if user_query.lower() in str(value).lower():
                    results.append({key: value})

        return results if results else ["No relevant information found for your query."]

    def clear_data(self):
        """
        Clear the currently loaded structured data.
        """
        self.structured_data = None
