# import pandas as pd
# import numpy as np
 
# df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f','h'],columns=['one', 'two', 'three'])

# df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

# print(df['one'].isnull())


# import pandas as pd
# import numpy as np

# df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
# 'h'],columns=['one', 'two', 'three'])

# df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

# print(df['one'].sum())


import pandas as pd
import numpy as np

df = pd.DataFrame({'one':[10,20,30,40,50,2000], 'two':[1000,0,30,40,50,60]})

print(df.replace({1000:10,2000:60,0:20}))