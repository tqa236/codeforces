import sys
from tqdm.std import tqdm
from joblib import Parallel, delayed

sys.setrecursionlimit(10 ** 9)
from math import ceil, log2

BEST_IC = {}


class TreeNode:
    def __init__(self, index, ic, height, parent):
        self.index = index
        self.ic = ic
        self.height = height
        self.parent = parent
        self.children = []


INT_MAX = TreeNode(None, None, float("inf"), None)

# A utility function to get
# minimum of two numbers
def minVal(x, y):
    if x == INT_MAX:
        return y
    if y == INT_MAX:
        return x
    return x if nodes[x - 1].height < nodes[y - 1].height else y


# A utility function to get the
# middle index from corner indexes.
def getMid(s, e):
    return s + (e - s) // 2


""" A recursive function to get the 
minimum value in a given range 
of array indexes. The following 
are parameters for this function. 
  
    st --> Pointer to segment tree 
    index --> Index of current node in the 
        segment tree. Initially 0 is 
        passed as root is always at index 0 
    ss & se --> Starting and ending indexes 
                of the segment represented 
                by current node, i.e., st[index] 
    qs & qe --> Starting and ending indexes of query range """


def RMQUtil(st, ss, se, qs, qe, index):

    # If segment of this node is a part
    # of given range, then return
    # the min of the segment
    if qs <= ss and qe >= se:
        return st[index]

    # If segment of this node
    # is outside the given range
    if se < qs or ss > qe:
        return INT_MAX
    # If a part of this segment
    # overlaps with the given range
    mid = getMid(ss, se)
    val1 = RMQUtil(st, ss, mid, qs, qe, 2 * index + 1)
    val2 = RMQUtil(st, mid + 1, se, qs, qe, 2 * index + 2)
    val = minVal(val1, val2)
    return val


# Return minimum of elements in range
# from index qs (query start) to
# qe (query end). It mainly uses RMQUtil()
def RMQ(st, n, qs, qe):

    # Check for erroneous input values
    if qs < 0 or qe > n - 1 or qs > qe:

        print("Invalid Input", n, qs, qe)
        return -1

    val = RMQUtil(st, 0, n - 1, qs, qe, 0)
    return val


# A recursive function that constructs
# Segment Tree for array[ss..se].
# si is index of current node in segment tree st
def constructSTUtil(arr, ss, se, st, si):

    # If there is one element in array,
    # store it in current node of
    # segment tree and return
    if ss == se:

        st[si] = arr[ss]
        return arr[ss]

    # If there are more than one elements,
    # then recur for left and right subtrees
    # and store the minimum of two values in this node
    mid = getMid(ss, se)
    st[si] = minVal(
        constructSTUtil(arr, ss, mid, st, si * 2 + 1),
        constructSTUtil(arr, mid + 1, se, st, si * 2 + 2),
    )

    return st[si]


"""Function to construct segment tree 
from given array. This function allocates 
memory for segment tree and calls constructSTUtil()
to fill the allocated memory """


def constructST(arr, n):
    # Allocate memory for segment tree

    # Height of segment tree
    x = (int)(ceil(log2(n)))

    # Maximum size of segment tree
    max_size = 2 * (int)(2 ** x) - 1

    st = [0] * (max_size)

    # Fill the allocated memory st
    constructSTUtil(arr, 0, n - 1, st, 0)

    # Return the constructed segment tree
    return st


def dfs(nodes, node):
    visited = [False for i in range(len(nodes))]

    # Create a stack for DFS
    stack = []

    # Push the current source node.
    euler = []
    stack.append(node)
    while stack:
        # Pop a vertex from stack and print it
        node = stack.pop()
        euler.append(node)
        # Stack may contain same vertex twice. So
        # we need to print the popped item only
        # if it is not visited.
        if not visited[node - 1]:
            visited[node - 1] = True

            # Get all adjacent vertices of the popped vertex s
            # If a adjacent has not been visited, then push it
            # to the stack.
            for n in nodes[node - 1].children[::-1]:
                if not visited[n - 1]:
                    stack.append(node)
                    stack.append(n)

    return euler


def find_first(euler, n):
    left = set(range(1, n + 1))
    first = [-1] * n
    for i, val in enumerate(euler):
        if val in left:
            left.remove(val)
            first[val - 1] = i
    return first


def read_input(file_name):
    with open(file_name, "r") as f:
        n = int(f.readline().strip())
        parents = [int(i) for i in f.readline().strip().split()]
        ics = [int(i) for i in f.readline().strip().split()]
        m = int(f.readline().strip())
        diseases = []
        for _ in range(m):
            diseases.append([int(i) for i in f.readline().strip().split()][1:])
        nq = int(f.readline().strip())
        patients = []
        for _ in range(nq):
            patients.append([int(i) for i in f.readline().strip().split()][1:])
    return n, parents, ics, m, diseases, nq, patients


def find_disease_single(q):
    for index, disease in enumerate(disease_reduced):
        if remove[index]:
            continue
        max_height = float("-inf")
        max_val = float("-inf")
        limit = nodes[q - 1].ic
        for qd in disease:
            if nodes[qd - 1].height < max_height:
                continue
            node = RMQ(
                st,
                ne,
                min(first[q - 1], first[qd - 1]),
                max(first[q - 1], first[qd - 1]),
            )
            max_val = max(max_val, nodes[node - 1].ic)
            max_height = max(max_height, nodes[node - 1].height)
            if max_val == limit:
                break
    return (q, index), max_val


def find_diseases(i, patient):
    max_score = float("-inf")
    max_score_limit = sum(nodes[i - 1].ic for i in patient)
    for index, disease in enumerate(disease_reduced):
        if remove[index]:
            continue
        ancester = RMQ(
            st,
            ne,
            min(
                first[patient_footprints[i] - 1],
                first[disease_footprints[index] - 1],
            ),
            max(
                first[patient_footprints[i] - 1],
                first[disease_footprints[index] - 1],
            ),
        )
        if ancester not in (patient_footprints[i], disease_footprints[index]):
            score = nodes[ancester - 1].ic * len(patient)
        else:
            score = 0
            for q in patient:
                if (q, index) in BEST_IC:
                    score += BEST_IC[(q, index)]
                    continue
                max_height = float("-inf")
                max_val = float("-inf")
                limit = nodes[q - 1].ic
                for qd in disease:
                    if nodes[qd - 1].height < max_height:
                        continue
                    node = RMQ(
                        st,
                        ne,
                        min(first[q - 1], first[qd - 1]),
                        max(first[q - 1], first[qd - 1]),
                    )
                    max_val = max(max_val, nodes[node - 1].ic)
                    max_height = max(max_height, nodes[node - 1].height)
                    if max_val == limit:
                        break
                score += max_val
                BEST_IC[(q, index)] = max_val
        if max_score < score:
            max_score = score
            max_disease = index + 1
            if max_score == max_score_limit:
                break
    return max_disease


def reduce_LCA(curr_nodes):
    node_set = set(curr_nodes)
    discard = set()
    skip = [False for i in range(len(curr_nodes))]
    for i in range(len(curr_nodes)):
        if skip[i]:
            continue
        for j in range(i + 1, len(curr_nodes)):
            if skip[j]:
                continue
            common = RMQ(
                st,
                ne,
                min(first[curr_nodes[i] - 1], first[curr_nodes[j] - 1]),
                max(first[curr_nodes[i] - 1], first[curr_nodes[j] - 1]),
            )
            if curr_nodes[i] == common:
                discard.add(curr_nodes[i])
                break
            if curr_nodes[j] == common:
                discard.add(curr_nodes[j])
                skip[j] = True
    result = node_set - discard
    return result


def find_footprint(curr_nodes):
    footprint = curr_nodes[0]
    for i in range(len(curr_nodes)):
        footprint = RMQ(
            st,
            ne,
            min(first[curr_nodes[i] - 1], first[footprint - 1]),
            max(first[curr_nodes[i] - 1], first[footprint - 1]),
        )
    return footprint


def find_lowest_node(node):
    ic = nodes[node - 1].ic
    child = node
    while len(nodes[child - 1].children) == 1:
        child = nodes[child - 1].children[0]
    return (child, ic)


def remove_duplicate(disease_reduced):
    remove = [False for _ in disease_reduced]
    for i in tqdm(range(len(disease_reduced))):
        if remove[i]:
            continue
        if len(disease_reduced[i]) > 1:
            continue
        for j in range(i + 1, len(disease_reduced)):
            if len(disease_reduced[j]) > 1:
                continue
            if lowest_nodes_diseases[i][0] == lowest_nodes_diseases[j][0]:
                if lowest_nodes_diseases[i][1] < lowest_nodes_diseases[j][1]:
                    remove[i] = True
                    break
                else:
                    remove[j] = True
    return remove


def solve(file_name):
    print("Read input")
    global nodes, st, ne, diseases, first, disease_reduced, remove, patient_footprints, disease_footprints, lowest_nodes_diseases
    n, parents, ics, m, diseases, nq, patients = read_input(file_name)
    print(n, m, nq)

    nodes = []
    root = TreeNode(1, ics[0], 0, None)
    nodes.append(root)
    heights = [0]
    for i, (parent, ic) in enumerate(zip(parents, ics[1:])):
        node = TreeNode(i + 2, ic, nodes[parent - 1].height + 1, parent)
        nodes.append(node)
        nodes[parent - 1].children.append(i + 2)
        heights.append(node.height)
    print("Build Euler Tour of Tree")
    euler = dfs(nodes, 1)

    print("Find first appearance")
    first = find_first(euler, n)
    # print(first)
    ne = len(euler)

    # Build segment tree from given array
    st = constructST(euler, ne)

    print("Reduce patient and disease symptoms")
    patient_reduced = []
    for i, patient in enumerate(tqdm(patients)):
        patient_reduced.append(reduce_LCA(patient))
    disease_reduced = []
    for i, disease in enumerate(tqdm(diseases)):
        disease_reduced.append(reduce_LCA(disease))

    lowest_nodes_diseases = []
    for i, disease in enumerate(tqdm(disease_reduced)):
        if len(disease) > 1:
            lowest_nodes_diseases.append(None)
        else:
            lowest_nodes_diseases.append(find_lowest_node(list(disease)[0]))
    print("Find footprint for patients and diseases")
    patient_footprints = [find_footprint(list(val)) for val in patient_reduced]
    disease_footprints = [find_footprint(list(val)) for val in disease_reduced]
    print("Remove duplicate")
    remove = remove_duplicate(disease_reduced)
    print(f"Remove {sum(remove)} diseases")

    # all_node_patients = set()
    # for i, patient in enumerate(tqdm(patients)):
    #     all_node_patients.update(set(patient))
    # best_ic_dict = Parallel(n_jobs=-1)(
    #     delayed(find_disease_single)(q) for q in all_node_patients
    # )
    # BEST_IC = {val[0]: val[1] for val in best_ic_dict}

    results = []
    print("Start diagnosing")
    for i, patient in enumerate(tqdm(patient_reduced)):
        max_disease = find_diseases(i, patient)
        results.append(max_disease)
    # results = Parallel(n_jobs=-1)(
    #     delayed(find_diseases)(patient) for patient in patients
    # )
    write_output(file_name, results)


def write_output(file_name, results):
    output_name = f"output2_{file_name}"

    with open(output_name, "w") as f:
        f.writelines("\n".join(map(str, results)) + "\n")


if __name__ == "__main__":
    # for i in range(5, 6):
    #     solve(f"{i}.txt")
    # solve(f"sample")
    # solve("test1")
    # solve(f"test2")
    solve(f"test3")
    # solve(f"test4")
    # solve("test5")
    # solve("test6")
    # solve("test7")
