/**
 * @param {string} S
 * @return {number[]}
 */
var partitionLabels = function(S) {
    const last = {}
    const partitions = []
    
    for (let i = 0; i < S.length; i++) {
        const char = S[i]
        
        last[char] = i
        
    }
    
    let i = 0;
    while (i < S.length) {
        const char = S[i]
        
        let nextIdx = last[char]
        let partition = char

        for(let j = i + 1; j <= nextIdx; j++) {
            const c = S[j]
            if (last[c] > nextIdx) {
                nextIdx = last[c]
            }
            partition += c
        }
        
        partitions.push(partition)
        i = nextIdx + 1
    } 
    
    const sizes = partitions.map((p) => p.length)
        
    return sizes
};