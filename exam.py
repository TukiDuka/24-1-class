# 1.b
# 2.b
# 3.c
# 4.a
# 5.c
# 6.a
# 7.c
# 7.c
# 8.c
# 9.a
# 10.d
# 11.b
# 12.b
13.
14.
# 15.c
# 16.a
# 17.b
# 18.c
# 19.
# 20.
# 21.
# 22.
# 1. Грэйди алгоритм - Минимум зоосны тоо

def greedy_coin_change(amount):
    # Зоосны төрөл
    coins = [25, 10, 5, 1]
    # Зоосны хуваарилалт
    coin_count = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin  # Зоосны тоог тооцоолно
            coin_count[coin] = count  # Хуваарилалтыг хадгална
            amount -= coin * count  # Үлдэгдлийг тооцоолно

    return coin_count

# Жишээ ашиглалт
amount = 120
result = greedy_coin_change(amount)
print("Зоосны хуваарилалт:")
for coin, count in result.items():
    print(f"{count}x{coin} тегрег")

# 2.Грэйди алгоритмын дагуу хамгийн бага зоосны тоог хэрхэн сонгох вэ?
def greedy_coin_change(amount, coins):
    coin_count = 0
    coin_used = []

    coins.sort(reverse=True)

    for coin in coins:
        while amount >= coin:
            amount -= coin
            coin_count += 1
            coin_used.append(coin)

    return coin_count, coin_used

amount = 100
coins = [1, 5, 10, 25]
count, used_coins = greedy_coin_change(amount, coins)

print(f"Хамгийн бага зоосны тоо: {count}")
print(f"Сонгосон зоосууд: {used_coins}")

#3.Асуулт 2: Аль алгоритм нь Грэйди алгоритмын зарчмыг ашиглан шийдэгддЭг вэ? хариулт:B

#4.Хаффман кодчилол Даалгавар 2:
# Тэмдэгтуудийн давтамж дээр ундэслен Хаффман код уусгэх Python програм бич. 
# Програм нь тэмдегтуудийг шахаж, хамгийн бага битээр хэрхэн илэрхийлахийг
# харуулна.


#5.Алгоритмын гуйцэтгэлийн ШИНЖИЛГЭЭ Acyyлт1: 0(n) гэж юуг илэрхийлдэг вэ? Хариулт: b) Алгоритмын хамгийн их боломжит гуйцэтгэлийг

# Бинар мод уусгэх ба хайлтын мод
# Даалгавар 4:
# Python дээр бинар хайлтын мод (Binary Search Tree) vycr, дараах үйлдлүүдийг гүйцэтгэнэ үү.
class TreeNode:
    def init(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def init(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_rec(node.right, key)

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search_rec(node.left, key)
        return self._search_rec(node.right, key)

    def find_min(self):
        return self._find_min_rec(self.root)

    def _find_min_rec(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.val

    def find_max(self):
        return self._find_max_rec(self.root)

    def _find_max_rec(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current.val

bst = BinarySearchTree()
values = [20, 9, 25, 5, 12, 15]
for value in values:
    bst.insert(value)

print("Minimum value:", bst.find_min()) 
print("Maximum value:", bst.find_max()) 
# Утга хайх
search_result_1 = bst.search(21)
print("Search 21:", "Found" if search_result_1 else "Not found")

search_result_2 = bst.search(18)
print("Search 18:", "Found" if search_result_2 else "Not found")

#Функц ба буцаах утга 
# Асуулт 1: Дараах функц ямар утга буцаах вэ? Хариулт: B
def test_func(x) : 
    if x%2==0:
        return x * 2
    else:
        return x+2
print(test_func(5))




