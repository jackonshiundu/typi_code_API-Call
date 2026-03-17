import requests
import json
def get_posts():
    url='https://jsonplaceholder.typicode.com/posts'

    try:
        response=requests.get(url)
        if response.status_code==200:
            posts= response.json()

            #Adding Json data to a file
            data={
                "posts": posts,
                "number_of_posts": len(posts)
            }
            with open('posts.json', 'w') as file:
                
                json.dump(data, file, indent=4)

            return posts
    except requests.RequestException as e:
        print(f"Error fetching posts: {e}")
        return None

def main():
    posts=get_posts()
    if posts:
        print(f"Fetched {len(posts)} posts from API.")
        print("Posts from API".center(50,"="))
        print("Title".center(50, "="))
        for post in posts:
            print(f"Post ID: {post['id']}, Title: {post['title']}")
    else:
        print('Failed to fetch posts from API.')
if __name__ == "__main__":
    main()