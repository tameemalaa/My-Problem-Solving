class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visted= []
        def fun(image,sr,sc,color):
            s_color = image[sr][sc]
            visted.append((sr,sc))
            image[sr][sc] = color 
            if (sr+1,sc) not in visted and sr != len(image)-1 and image[sr+1][sc] == s_color :
                fun(image,sr+1,sc,color)
            if (sr-1,sc) not in visted and sr!=0 and image[sr-1][sc] == s_color: 
                fun(image,sr-1,sc,color)
            if (sr,sc+1) not in visted and sc!= len(image[sr])-1 and image[sr][sc+1] == s_color: 
                fun(image,sr,sc+1,color)
            if (sr,sc-1) not in visted and sc!=0 and image[sr][sc-1] == s_color: 
                fun(image,sr,sc-1,color)
            return
        fun(image,sr,sc,color)
        return image