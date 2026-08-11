class Solution(object):
    def hasPathSum(self, root, targetSum):

        def dfs(node, curSum):
            if not node:
                return False

            curSum += node.val

            # If it's a leaf, check the sum
            if not node.left and not node.right:
                return curSum == targetSum

            # Otherwise, search both subtrees
            return dfs(node.left, curSum) or dfs(node.right, curSum)

        return dfs(root, 0)

        