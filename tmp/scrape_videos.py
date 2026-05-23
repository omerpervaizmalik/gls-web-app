import urllib.request
import re
import json

url = "https://www.youtube.com/@LawUntold/videos"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    # Find the ytInitialData JSON in the page HTML
    match = re.search(r'var ytInitialData = ({.*?});</script>', html)
    if not match:
        # Try without var
        match = re.search(r'window\["ytInitialData"\] = ({.*?});', html)
        
    if match:
        data_str = match.group(1)
        data = json.loads(data_str)
        
        # Traverse the nested ytInitialData structure to extract videos
        videos = []
        try:
            # Navigate to the video tabs contents
            tabs = data['contents']['twoColumnBrowseResultsRenderer']['tabs']
            videos_tab = None
            for tab in tabs:
                if 'tabRenderer' in tab and tab['tabRenderer'].get('selected', False):
                    videos_tab = tab['tabRenderer']
                    break
            if not videos_tab:
                # Find by title
                for tab in tabs:
                    if 'tabRenderer' in tab and 'videos' in tab['tabRenderer'].get('title', '').lower():
                        videos_tab = tab['tabRenderer']
                        break
            
            contents = videos_tab['content']['richGridRenderer']['contents']
            for content in contents:
                if 'richItemRenderer' in content:
                    item = content['richItemRenderer']['content']
                    if 'videoRenderer' in item:
                        video = item['videoRenderer']
                        video_id = video['videoId']
                        title = video['title']['runs'][0]['text']
                        
                        duration = "Watch"
                        if 'lengthText' in video:
                            duration = video['lengthText']['simpleText']
                            
                        views = "YouTube Video"
                        if 'viewCountText' in video and 'simpleText' in video['viewCountText']:
                            views = video['viewCountText']['simpleText']
                        elif 'viewCountText' in video and 'runs' in video['viewCountText']:
                            views = "".join([r['text'] for r in video['viewCountText']['runs']])
                            
                        date = "Recent"
                        if 'publishedTimeText' in video:
                            date = video['publishedTimeText']['simpleText']
                            
                        videos.append({
                            "title": title,
                            "youtubeId": video_id,
                            "duration": duration,
                            "views": views,
                            "date": date
                        })
        except Exception as e:
            print(f"Error traversing JSON structure: {e}")
            
        print(f"SUCCESS: Found {len(videos)} videos.")
        # Write to JSON file
        with open('d:\\Anti gravity\\get-legal-solution\\tmp\\scraped_videos.json', 'w', encoding='utf-8') as f:
            json.dump(videos, f, indent=4, ensure_ascii=False)
    else:
        print("ERROR: ytInitialData not found in HTML.")
except Exception as e:
    print(f"Network or parsing error: {e}")
