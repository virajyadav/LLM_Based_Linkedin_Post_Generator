import json
import pandas as pd



class FewShort:

    def __init__(self, file_path="processed_data/dhaval_post.json"):
        self.df = None
        self.unique_tags = None
        self.load_data(file_path)

    def load_data(self, file_path):
        with open(file_path, encoding='utf-8') as file:
            post = json.load(file)
            self.df = pd.json_normalize(post)
            self.df['length'] = self.df['line_count'].apply(self.categorize_length)
            self.unique_tags = self.df['tags'].explode().unique()
            

    def get_unique_tags(self):
        return self.unique_tags

    def categorize_length(self, line_count):
        if line_count <= 6:
            return "Short"
        elif line_count >= 11 and line_count <= 23:
            return "Medium"
        else:
            return "Long"
        
    def get_filtered_df(self, length,language,tag):
        filtered_df = self.df[(self.df['length'] == length) & (self.df['language'] == language) & (self.df['tags'].apply(lambda x: tag in x))]
        return filtered_df.to_dict(orient='records')
if __name__ == "__main__":
    fs = FewShort()
    print(fs.get_filtered_df("Long","English","Motivation"))

