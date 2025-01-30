import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm


def preprocess_post(post_file_path, output_file_path):
    enriched_posts = []
    with open(post_file_path, encoding='utf-8') as file:
        posts = json.load(file)
        for post in posts:
            post_with_metadata = post | extract_metadata(post)
            enriched_posts.append(post_with_metadata)
        unique_tags = get_unique_tags(enriched_posts)
        print("Unique tags: ", unique_tags)
        for post in enriched_posts:
            current_tags = post["tags"]
            new_tags = {unique_tags.get(tag, tag) for tag in current_tags}
            post['tags'] = list(new_tags)
        
    with open(output_file_path, encoding='utf-8', mode="w") as outfile:
            json.dump(enriched_posts, outfile, indent=4)


def get_unique_tags(posts_with_metadata):
    unique_tags = set()
    for post in posts_with_metadata:
        unique_tags.update(post["tags"])
    unique_tags_list = ', '.join(unique_tags)

    template = '''I will give you a list of tags. You need to unify tags with the following requirements,
    1. Tags are unified and merged to create a shorter list. 
       Example 1: "Jobseekers", "Job Hunting" can be all merged into a single tag "Job Search". 
       Example 2: "Motivation", "Inspiration", "Drive" can be mapped to "Motivation"
       Example 3: "Personal Growth", "Personal Development", "Self Improvement" can be mapped to "Self Improvement"
       Example 4: "Scam Alert", "Job Scam" etc. can be mapped to "Scams"
    2. Each tag should be follow title case convention. example: "Motivation", "Job Search"
    3. Output should be a JSON object, No preamble
    3. Output should have mapping of original tag and the unified tag. 
       For example: {{"Jobseekers": "Job Search",  "Job Hunting": "Job Search", "Motivation": "Motivation}}
    
    Here is the list of tags: 
    {tags}
    '''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={"tags":str(unique_tags_list)})
    try:
        json_parser = JsonOutputParser()
        return json_parser.parse(response.content)
    except OutputParserException as e:
        print(f"Error parsing JSON: {e}")
    

def extract_metadata(post):
    template = '''
    You are given a LinkedIn post. You need to extract number of lines, language of the post and tags.
    1. Return a valid JSON. No preamble. 
    2. JSON object should have exactly three keys: line_count, language and tags. 
    3. tags is an array of text tags. Extract maximum two tags.
    4. Language should be English or Hinglish (Hinglish means hindi + english)
    
    Here is the actual post on which you need to perform this task:  
    {post}
    '''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={"post":post})
    try:
        json_parser = JsonOutputParser()
        return json_parser.parse(response.content)
    except OutputParserException as e:
        print(f"Error parsing JSON: {e}")
        

if __name__ == "__main__":
    preprocess_post("raw_data/dhaval_post.json", "processed_data/dhaval_post.json")
