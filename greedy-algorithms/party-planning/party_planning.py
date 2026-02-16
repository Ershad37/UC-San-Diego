from collections import defaultdict


def main():
    print(max_independent_set([[1, 2], [2, 3], [3, 4]]))


def max_independent_set(edges):
    children = defaultdict(list)
    nodes = set()
    child_nodes = set()

    for parent, child in edges:
        children[parent].append(child)
        nodes.add(parent)
        nodes.add(child)
        child_nodes.add(child)

    root = (nodes - child_nodes).pop()

    def dfs(node):
        include = 1
        exclude = 0
        for child in children[node]:
            child_include, child_exclude = dfs(child)

            include += child_exclude

            exclude += max(child_include, child_exclude)

        return include, exclude

    include_root, exclude_root = dfs(root)

    return max(include_root, exclude_root)


if __name__ == "__main__":
    main()
