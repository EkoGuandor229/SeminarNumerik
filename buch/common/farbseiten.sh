awk 'BEGIN {
	result = ""
	counter = 0
} 
{
	if (length(result) == 0) {
		result = $1
	} else {
		result = sprintf("%s,%d", result, $1)
	}
	counter++
}
END {
	printf("%s\n", result)
	printf("Anzahl Farbseiten: %d\n", counter)
}' <<EOF
13
16
17
19
21
23
24
25
29
30
31
34
37
42
45
49
50
52
53
55
59
65
71
72
74
76
77
78
84
85
87
88
90
91
95
100
104
107
109
110
110
113
114
116
117
120
122
123
125
140
149
150
154
155
161
163
167
170
177
187
189
190
191
192
197
204
209
210
216
217
219
220
224
225
226
228
229
230
232
233
235
236
239
241
245
246
251
EOF
