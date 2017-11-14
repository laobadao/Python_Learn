"""
 [10. Regular Expression Matching]

 https://leetcode.com/problems/regular-expression-matching/

 Question：正则表达式匹配
 Method：DP - dynamic programming 动态规划

Implement regular expression matching with support for '.' and '*'.
实现正则表达式，支持'.' and '*'

'.' Matches any single character. '.' 点匹配任何字母
'*' Matches zero or more of the preceding element. 匹配 0个 或更多元素

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)
（字符串，匹配规则）
Some examples:
isMatch(“aa”,”a”) → false “aa” 俩字母 ，”a”一个字母 aa 不符合 a 这个正则表达式
isMatch(“aa”,”aa”) → true
isMatch(“aaa”,”aa”) → false
isMatch(“aa”, “a*”) → true “aa” 符合 a* ,开头字母是 a 后面的字母任意
isMatch(“aa”, “.*”) → true
isMatch(“ab”, “.*”) → true
isMatch(“aab”, “c*a*b”) → true ？？？

为什么 isMatch(“aab”, “c*a*b”) → true ？

因为：'*' Matches zero or more of the preceding element. 匹配 0个 或更多元素

So for this testcase "c* a* b" could be 0 c 2 a and 1 b, it matched aab

"c* a* b"  ，这么看 * 代表0 个或多个，所以就是 0个 或多个 c ,0个 或多个 a ,一个b

所以 aab 满足，0个 c,2 个 a,一个 b


"""

"""
part1:

Without a Kleene star'*', our solution would look like this:
没有 * ，不含通配符 * 的情况下
"""


def match(text, pattern):
    if not pattern:
        return not text
    # pattern[0] pattern 里面第 0 个元素在 {text[0], '.'} 这个字典中，
    # {text[0], '.'} 这个字典包含 text 里 第 0 个元素 和 '.'
    # bool(text) 1. 若 text = "abba"  print('bool(text)'True
    # text = ""  print('bool(text)') False ,也就是 bool(text)  测试 text 不为空
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    # match() 方法递归循环的 去做判断，每一个字母的匹配，返回的是布尔 Boolean 类型
    # text[1:] 代表 从 索引 1 开始包含索引1 的元素 ，也就是不包含索引0 的元素
    return first_match and match(text[1:], pattern[1:])


def learn_bool():
    text = "abba"
    print('bool(text)', bool(text))  # True
    text = ""
    print('bool(text)', bool(text))  # False
    return bool(text)


"""
part 2:
If a star is present in the pattern, it will be in the second position 
pattern[1]. Then, we may ignore this part of the pattern, 
or delete a matching character in the text. 
If we have a match on the remaining strings after any of these operations,
 then the initial inputs matched.

含有 * 的情況下，

"""


class Solution(object):
    def isMatch(self, text, pattern):
        # 判断不为空
        if not pattern:
            return not text
        # 因为如果包含 * ，则 肯定是从索引 1 开始有 * ，则索引 0 位的元素 需要判断下 是否匹配
        first_match = bool(text) and pattern[0] in {text[0], '.'}
        # 若 pattern 的长度 >= 2 ，且索引 1 位的元素是 *
        if len(pattern) >= 2 and pattern[1] == '*':
            # 1. self.isMatch(text, pattern[2:])
            # pattern[2:] 从索引为 2 的元素开始，包含索引 2 的元素，
            # 例如 a*bb,则 pattern 则 忽略前面的  a* ，从 bb 往后作为 pattern
            # 2.self.isMatch(text, pattern[2:]) or first_match 其中有一个是真
            # 也就是 若 first_match 是 false ，比如 (bbb,a*bbb)
            # b and a not equal ,a*bbb means  0 or more a and 3 b ,then True
            # 3.self.isMatch(text[1:], pattern) --text 从 索引1 开始，包含 1 然后再与 原 pattern 进行匹配
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            # 如果 pattern[1] 索引1 的位置不是 * text[1:], pattern[1:] 都从 索引1 位置取，递归
            return first_match and self.isMatch(text[1:], pattern[1:])


def test(text, pattern):
    # print(test("eee", ""))  # False
    # print(test("eee", "eee"))  # None
    if not pattern:
        return not text


if __name__ == '__main__':
    print(test("eee", ""))  # False
    print(test("eee", "eee"))  # None