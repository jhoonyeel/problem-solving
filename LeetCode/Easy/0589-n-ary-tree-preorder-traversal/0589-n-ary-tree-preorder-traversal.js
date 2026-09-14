/**
 * // Definition for a _Node.
 * function _Node(val, children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {_Node|null} root
 * @return {number[]}
 */
var preorder = function (root) {
    const res = [];

    // 재귀는 "나"를 기준으로 생각. 나 === 현재 node.
    // 1. 내가 null인 경우 즉시 리턴
    // 2. 나의 val를 push
    // 3. 나의 children 순회하면서, children의 각 요소(노드의 묶음)를 다음 "나"로 지정.
    function dfs(node) {
        if (node === null) {
            return;
        }

        res.push(node.val)
        for (const nxt_node of node.children) {
            dfs(nxt_node);
        }
    }

    dfs(root);

    return res;
};