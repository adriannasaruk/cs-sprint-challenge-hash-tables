# Your code here



def finder(files, queries):
    cache = {}

    for paths in files:
        file = paths.split('/')[-1]

        if file in cache:
            cache[file].append(paths)
        else:
            cache[file] = [paths]
    # Your code here
    
    result = []

    for query in queries:
        if query in cache:
            results = cache[query]
            for paths in results:
                result.append(paths)
                print(result)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
