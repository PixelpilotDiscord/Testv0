def view_video():
    headers = {
        'User-Agent': generate_user_agent(),
        'X-Forwarded-For': generate_ip_address()
    }
    match = re.search(r"(?:v=|youtu\.be\/)([-\w]+)", video_url)
    if match:
        video_id = match.group(1)
        data = {
            'event': 'watch',
            'video_id': video_id
        }
        requests.post(
            'https://www.youtube.com/watch_ajax',
            data=data,
            headers=headers
        )
    else:
        print("Invalid video URL")
