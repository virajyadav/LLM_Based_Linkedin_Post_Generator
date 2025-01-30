from llm_helper import llm
from few_short import FewShort

fs = FewShort()

def get_length_str(length):
    if length == "Short":
        return "1 to 6 lines"
    if length == "Medium":
        return "11 to 23 lines"
    if length == "Long":
        return "24 to 30 lines"
    

def generate_post(tag, length,language):
    #prompt = f"Generate a LinkedIn post for the tag {tag} with the length {get_length_str(length)} in the language {language}"
    prompt = get_prompt(length, language, tag)
    response = llm.invoke(prompt)
    return response.content


def get_prompt(length, language, tag):
    length_str = get_length_str(length)

    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.
    Make this suitable for Design Enginner for mechanical part using catia v5.

    1) Topic: {tag}
    2) Length: {length_str}
    3) Language: {language}
    The script for the generated post should always be English.
    '''
    # prompt = prompt.format(post_topic=tag, post_length=length_str, post_language=language)

    examples = fs.get_filtered_df(length, language, tag)

    if len(examples) > 0:
        prompt += "4) Use the writing style as per the following examples."

    for i, post in enumerate(examples):
        post_text = post['text']
        prompt += f'\n\n Example {i+1}: \n\n {post_text}'

        if i == 1:
            break

    return prompt


if __name__ == "__main__":
    #print(get_prompt("Short", "English", "Artificial Intelligence"))
    print(generate_post("Short", "English", "Artificial Intelligence"))
