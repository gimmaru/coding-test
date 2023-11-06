def solution(today, terms, privacies):
    deadline = dict()
    for term in terms:
        t, end = term.split(" ")
        deadline[t] = int(end) * 28
    
    y_today, m_today, d_today = today.split('.')
    y_today, m_today, d_today = int(y_today), int(m_today), int(d_today)
    
    answer = []
    for idx, privacy in enumerate(privacies, 1):
        start, t = privacy.split(" ")
        time = 0
        
        y_start, m_start, d_start = start.split('.')
        y_start, m_start, d_start = int(y_start), int(m_start), int(d_start)
        
        if d_today < d_start:
            m_today -= 1
            d_today += 28
        
        time += (y_today - y_start) * 28 * 12
        time += (m_today - m_start) * 28
        time += (d_today - d_start)
        
        if time >= deadline[t]:
            answer.append(idx)
    return answer

def solution(today, terms, privacies):
    answer = []

    deadline = dict()
    for term in terms:
        t, end = term.split(" ")
        deadline[t] = int(end) * 28
    
    def convert_to_day(yyyy_mm_dd):
        y, m, d = map(int, yyyy_mm_dd.split("."))
        return y * 28 * 12 + m * 28 + d

    today = convert_to_day(today)
    for idx, privacy in enumerate(privacies, 1):
        start, t = privacy.split(" ")
        start = convert_to_day(start)
        if deadline[t] >= today - start:
            answer += idx,
    return answer