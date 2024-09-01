def remove_url_anchor(url):
    ind = 0
    for i in url:
        if "#" in url:
            ind = url.index("#") 
            return url[:ind]
        else:
            return url
    
    