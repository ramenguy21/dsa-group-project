from PIL import Image


# A Huffman Tree Node
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq
 
        # symbol name (charecter)
        self.symbol = symbol
 
        # node left of current node
        self.left = left
 
        # node right of current node
        self.right = right
 
        # tree direction (0/1)
        self.huff = ''

class pixel_node:
    #Define node construction method
    def __init__(self,right=None,left=None, parent=None, weight=0, code=None):
        self.left = left 
        self.right = right 
        self.parent = parent 
        self.weight = weight #weight
        self.code = code #Node value
 
# utility function to print huffman
# codes for all symbols in the newly
# created Huffman tree
 
 
def printNodes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.huff)
 
    # if node is not an edge node
    # then traverse inside it
    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)
 
        # if node is edge node then
        # display its huffman code
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")
 

# charecters for huffman tree
chars = ['a', 'b', 'c', 'd', 'e', 'f']
 
# frequency of charecters
freq = [ 5, 9, 12, 13, 16, 45]
 
# list containing unused nodes
nodes = []
 
# converting ccharecters and frequencies
# into huffman tree nodes
for x in range(len(chars)):
    nodes.append(node(freq[x], chars[x]))
 
while len(nodes) > 1:
    # sort all the nodes in ascending order
    # based on theri frequency
    nodes = sorted(nodes, key=lambda x: x.freq)
 
    # pick 2 smallest nodes
    left = nodes[0]
    right = nodes[1]
 
    # assign directional value to these nodes
    left.huff = 0
    right.huff = 1
 
    # combine the 2 smallest nodes to create
    # new node as their parent
    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
 
    # remove the 2 nodes and add their
    # parent as new node among others
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)
 
printNodes(nodes[0])

def pixel_frequency(pxl_lst):
    pxl_freq = {}
    for i in pxl_lst:
        if i not in pxl_freq.keys():
            pxl_freq[i] = 1
        else:
            pxl_freq[i] += 1
    return pxl_freq

def construct_node(pixel):
    node_lst = []
    for i in range(len(pixel)):
        node_lst.append(pixel_node(weight = pixel[i][1], code=str(pixel[i][0])))
    return node_lst

def construct_tree(node_lst):
    node_lst = sorted(node_lst ,key=lambda pixel_node:pixel_node.weight) 
    while(len(node_lst) != 1):
        #0 is left, 1 is right
        node0, node1 = node_lst[0], node_lst[1]
        merge_node = pixel_node(left=node0, right=node1, weight=node0.weight + node1.weight)
        node0.parent = merge_node
        node1.parent = merge_node
        node_lst.remove(node0)
        node_lst.remove(node1)
        node_lst.append(merge_node)
        node_lst = sorted(node_lst ,key=lambda pixel_node:pixel_node.weight) 
    return node_lst

def huffman_encoding(img):
    width = img.size[0]
    height = img.size[1]
    im = img.load()
    pixel_lst = []
    for i in range(width):
        for j in range(height):
            pixel_lst.append(im[i, j])

    pixel_freq = pixel_frequency(pixel_lst)
    pixel_freq = sorted(pixel_freq.items(), key=lambda item:item[1])
    node_lst = construct_node(pixel_freq)
    huff_tree_head = construct_tree(node_lst)[0]
    encoding_table = {}

    for x in node_lst:
        curr_node = x
        encoding_table.setdefault(x.code, "")
        while(curr_node != huff_tree_head):
            if curr_node.parent.left == curr_node:
                encoding_table[x.code] = "1" + encoding_table[x.code]
            else:
                encoding_table[x.code] = "0" + encoding_table[x.code]
            curr_node = curr_node.parent

    for key in encoding_table.keys():
        print("Source Pixel: " + key + "\nCode Strength after encoding:" + encoding_table[key])
    print("Encoding Table: ", encoding_table)

def decoding(w, h, encoding_table, coding_res):
    code_read_now = ''  # The currently read code
    new_pixel =[] 
    i = 0
    while (i != coding_res.__len__()):
                 #Read one later each time
        code_read_now = code_read_now + coding_res[i]
        for key in encoding_table.keys():
                         #If the currently read code exists in the code table 
            if code_read_now == encoding_table[key]: 
                new_pixel. append(key) 
                code_read_now = ' '
                break
        i +=1
         #Construct a new image
    decode_image = Image.new( 'L' ,(w,h)) 
    k = 0 
         # 
    for i in range(w):
        for j in range(h):
            decode_image.putpixel((i,j),(int(new_pixel[k]))) 
        k+=1
    decode_image.save('decode.bmp') 
    print("Decoding has been completed: the picture is stored as decode.bmp")


img = Image.open('tiger.bmp')
g_img = img.convert('L')
huffman_encoding(g_img)
print("ended")
