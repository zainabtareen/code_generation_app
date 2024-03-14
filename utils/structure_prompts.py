
def gen_code_input(description, language):
    messages=[
    {"role": "system", "content": f"You are a helpful code assistant who can write professional code. Your language of choice is {language}. Never try to explain anything, just generate the code."},
    {"role": "user", "content": f"Generate the {language} code which meets the requirements mentioned below:\n{description}"},
    ]
    return messages

def feedback_code_input(description_w_fb, language):
    content = description_w_fb.split('***Feedback***')
    fb = '\n\n'.join([cn.strip() for cn in content[1:]])
    s = "s" if len(fb)>1 else ""
    messages=[
    {"role": "system", "content": f"You are a helpful code assistant who can write professional code. Your language of choice is {language}. You have already attempted {len(fb)} time{s} to generated the code according to the requirements provided by user. The user has given feedback on your previously written code block{s}. This time, you are expected to write the best code according to the requirements and all the feedback provided by the user. Never try to explain anything, just generate the code."},
    {"role": "user", "content": f"Requirements:\n{content[0]}"},
    {"role": "user", "content": f"Feedback:\n\n{fb}"}
    ]
    return messages