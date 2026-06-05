import requests
from bs4 import BeautifulSoup

def test_login():
    url = "https://pakistanlawsite.com/Login/MainPage"
    session = requests.Session()
    
    # Provide a real-looking user agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    print("Fetching login page...")
    try:
        r = session.get(url, headers=headers, verify=False)
        print(f"Status Code: {r.status_code}")
        soup = BeautifulSoup(r.text, 'html.parser')
        
        # Look for forms and inputs
        forms = soup.find_all('form')
        print(f"Found {len(forms)} forms.")
        
        login_form = None
        for form in forms:
            if form.get('action') and 'MainPage' in form.get('action'):
                login_form = form
                break
        
        if not login_form:
            login_form = forms[0] # assume first is login

        form_data = {}
        for i in login_form.find_all('input'):
            name = i.get('name')
            value = i.get('value', '')
            if name:
                form_data[name] = value
                
        form_data['Login.UserName'] = 'sjdgkhan'
        form_data['Login.Password'] = 'law12345'
                
        print("Submitting login to:", login_form.get('action'))
        post_url = url
        if login_form.get('action'):
            post_url = f"https://pakistanlawsite.com{login_form.get('action')}"
            
        r_post = session.post(post_url, data=form_data, headers=headers, verify=False, allow_redirects=False)
        print(f"Post status: {r_post.status_code}")
        print("Location header:", r_post.headers.get('Location'))
        
        # Follow redirect if any
        if r_post.status_code in (301, 302):
            r_post = session.get(f"https://pakistanlawsite.com{r_post.headers.get('Location')}", headers=headers, verify=False)
            
        print("Final URL:", r_post.url)
        if r_post.text.strip().strip('"') == "/Login/Check":
            session.get("https://pakistanlawsite.com/Login/Check", headers=headers, verify=False, allow_redirects=True)
            
            # Fetch the main dashboard
            r_dash = session.get("https://pakistanlawsite.com/Home/Dashboard", headers=headers, verify=False)
            if r_dash.status_code == 404:
                 r_dash = session.get("https://pakistanlawsite.com/", headers=headers, verify=False)
                 
            soup = BeautifulSoup(r_dash.text, 'html.parser')
            print("Saving dashboard HTML...")
            with open("dashboard.html", "w", encoding="utf-8") as f:
                f.write(r_dash.text)
            print("Login SUCCESSFUL and dashboard saved to dashboard.html")
            
            print("Fetching Judgment 2026P2004...")
            r_case = session.post("https://pakistanlawsite.com/Login/GetCaseFile", data={"caseName": "2026P2004", "headNotes": 0}, headers=headers, verify=False)
            
            if r_case.status_code == 200:
                print(f"Judgment fetched successfully! Length: {len(r_case.text)}")
                print(r_case.text[:1000])
                
                # Check what type of data it is (JSON or HTML)
                try:
                    import json
                    data = r_case.json()
                    print("Response is JSON!")
                except json.JSONDecodeError:
                    print("Response is HTML/Text!")
            else:
                print(f"Failed to fetch judgment: Status Code {r_case.status_code}")
        else:
            print("Login FAILED (no valid redirect string).")
            print("Raw Response Output:", r_post.text[:500])
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import urllib3
    urllib3.disable_warnings()
    test_login()
