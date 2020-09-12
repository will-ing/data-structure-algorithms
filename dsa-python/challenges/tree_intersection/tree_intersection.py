def intersection(tree, tree_two):
    while tree.root:
        value = tree.root.val
        duplicates(value, tree_two)


def duplicates(val, tree):
    tree_list = []
    while tree.root:
        if val == tree.root.val:
            tree_list.append(val)
        else:
            tree.root = tree.root.right_child
