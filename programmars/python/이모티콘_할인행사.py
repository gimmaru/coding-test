def solution(users, emoticons):
    answer = [float('-inf'), float('-inf')]
    
    def product(m, discounts=[10, 20, 30, 40]):
        result = []
        def dfs(accmul, m, discounts=discounts):
            if m == 0:
                result.append(accmul)
                return None

            for discount in discounts:
                dfs(accmul + [discount], m - 1)
        dfs([], m)
        return result
        
    for discounts in product(len(emoticons), [10, 20, 30, 40]):
        members, sales = 0, 0
        
        for cri, member in users:
            sales_per_user = 0
            
            for discount, price in zip(discounts, emoticons):
                if discount >= cri:
                    sales_per_user += price - int(price * (discount / 100))
                
            if sales_per_user >= member:
                members += 1
            else:
                sales += sales_per_user
        
        if members > answer[0] or (members == answer[0] and sales > answer[1]):
            answer = [members, sales]
        
    return answer