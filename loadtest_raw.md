[2026-02-07 16:34:09,306] Parimals-MacBook-Air/INFO/locust.main: Starting Locust 2.34.0
[2026-02-07 16:34:09,306] Parimals-MacBook-Air/WARNING/locust.main: Python 3.9 support is deprecated and will be removed soon
[2026-02-07 16:34:09,308] Parimals-MacBook-Air/INFO/locust.main: Run time limit set to 60 seconds
Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                         0     0(0.00%) |      0       0       0      0 |    0.00        0.00

[2026-02-07 16:34:09,308] Parimals-MacBook-Air/INFO/locust.runners: Ramping to 20 users at a rate of 5.00 per second
Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
POST     /v1/quiz/answer                                                                    1     0(0.00%) |     35      35      35     35 |    0.00        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              1   1(100.00%) |     24      24      24     24 |    0.00        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              1   1(100.00%) |     74      74      74     74 |    0.00        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          1     0(0.00%) |     92      92      92     92 |    0.00        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          1     0(0.00%) |     83      83      83     83 |    0.00        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          1     0(0.00%) |     37      37      37     37 |    0.00        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          1     0(0.00%) |     39      39      39     39 |    0.00        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          1     0(0.00%) |    122     122     122    122 |    0.00        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          1     0(0.00%) |    123     123     123    123 |    0.00        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                          1     0(0.00%) |     70      70      70     70 |    0.00        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          1     0(0.00%) |     69      69      69     69 |    0.00        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                        11    2(18.18%) |     70      24     123     71 |    0.00        0.00

[2026-02-07 16:34:12,320] Parimals-MacBook-Air/INFO/locust.runners: All users spawned: {"QuizUser": 20} (20 total users)
Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                              1     0(0.00%) |     29      29      29     29 |    0.00        0.00
GET      /v1/leaderboard/streak                                                             1     0(0.00%) |      7       7       7      7 |    0.00        0.00
POST     /v1/quiz/answer                                                                   10     0(0.00%) |     29      12      89     23 |    0.00        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              1   1(100.00%) |     24      24      24     24 |    0.50        0.50
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              2    1(50.00%) |     43      12      74     13 |    0.50        0.50
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              1     0(0.00%) |      7       7       7      7 |    0.00        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          2     0(0.00%) |     55      18      92     19 |    0.50        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          1     0(0.00%) |     83      83      83     83 |    0.50        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                          1     0(0.00%) |     25      25      25     25 |    0.00        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          1     0(0.00%) |     87      87      87     87 |    0.00        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          1     0(0.00%) |     40      40      40     40 |    0.00        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          1     0(0.00%) |    102     102     102    102 |    0.00        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          1     0(0.00%) |     37      37      37     37 |    0.50        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          1     0(0.00%) |     39      39      39     39 |    0.50        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                          1     0(0.00%) |     40      40      40     40 |    0.00        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          1     0(0.00%) |     34      34      34     34 |    0.00        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          1     0(0.00%) |    122     122     122    122 |    0.50        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                          1     0(0.00%) |     90      90      90     90 |    0.00        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          1     0(0.00%) |    123     123     123    123 |    0.50        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                          2     0(0.00%) |     40       9      70      9 |    0.50        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                          2     0(0.00%) |     50       7      93      7 |    0.00        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          1     0(0.00%) |     97      97      97     97 |    0.00        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                          1     0(0.00%) |     97      97      97     97 |    0.00        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          1     0(0.00%) |     69      69      69     69 |    0.50        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                        38     2(5.26%) |     48       7     123     34 |    5.00        1.00

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                              4     0(0.00%) |     14       7      29      9 |    0.25        0.00
GET      /v1/leaderboard/streak                                                             4     0(0.00%) |      8       5      16      7 |    0.25        0.00
POST     /v1/quiz/answer                                                                   21    5(23.81%) |     24      12      89     22 |    2.00        0.00
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              1     0(0.00%) |     10      10      10     10 |    0.00        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              1   1(100.00%) |     24      24      24     24 |    0.25        0.25
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              2    1(50.00%) |     43      12      74     13 |    0.50        0.25
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              1     0(0.00%) |      7       7       7      7 |    0.25        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          2     0(0.00%) |     55      18      92     19 |    0.25        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          2     0(0.00%) |     50      17      83     17 |    0.25        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                          2     0(0.00%) |     21      17      25     18 |    0.25        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          1     0(0.00%) |     87      87      87     87 |    0.25        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          1     0(0.00%) |     16      16      16     16 |    0.25        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          1     0(0.00%) |     40      40      40     40 |    0.25        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          1     0(0.00%) |    102     102     102    102 |    0.25        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          1     0(0.00%) |     37      37      37     37 |    0.25        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          2     0(0.00%) |     30      21      39     21 |    0.25        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                          1     0(0.00%) |     40      40      40     40 |    0.25        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          1     0(0.00%) |     34      34      34     34 |    0.25        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          1     0(0.00%) |    122     122     122    122 |    0.25        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                          1     0(0.00%) |     90      90      90     90 |    0.25        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          1     0(0.00%) |    123     123     123    123 |    0.25        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                          2     0(0.00%) |     40       9      70      9 |    0.50        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                          3     0(0.00%) |     38       7      93     16 |    0.50        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          1     0(0.00%) |     97      97      97     97 |    0.25        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                          1     0(0.00%) |     97      97      97     97 |    0.25        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          1     0(0.00%) |     69      69      69     69 |    0.25        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                          1     0(0.00%) |     23      23      23     23 |    0.00        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                        61    7(11.48%) |     36       5     123     23 |    8.75        0.50

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                              5     0(0.00%) |     13       7      29     12 |    0.50        0.00
GET      /v1/leaderboard/streak                                                             5     0(0.00%) |      8       4      16      7 |    0.50        0.00
POST     /v1/quiz/answer                                                                   30   13(43.33%) |     22      12      89     17 |    3.17        0.67
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              1     0(0.00%) |     10      10      10     10 |    0.17        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              1   1(100.00%) |     24      24      24     24 |    0.17        0.17
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              2    1(50.00%) |     43      12      74     13 |    0.33        0.17
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              1     0(0.00%) |      7       7       7      7 |    0.17        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              1     0(0.00%) |     12      12      12     12 |    0.00        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          2     0(0.00%) |     55      18      92     19 |    0.33        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          2     0(0.00%) |     50      17      83     17 |    0.17        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                          2     0(0.00%) |     21      17      25     18 |    0.17        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          1     0(0.00%) |     87      87      87     87 |    0.17        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          1     0(0.00%) |     16      16      16     16 |    0.17        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          2     0(0.00%) |     30      20      40     20 |    0.17        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          1     0(0.00%) |    102     102     102    102 |    0.17        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          1     0(0.00%) |     37      37      37     37 |    0.17        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          3     0(0.00%) |     27      21      39     21 |    0.33        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                          2     0(0.00%) |     28      16      40     17 |    0.17        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          1     0(0.00%) |     34      34      34     34 |    0.17        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          1     0(0.00%) |    122     122     122    122 |    0.17        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                          1     0(0.00%) |     90      90      90     90 |    0.17        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          1     0(0.00%) |    123     123     123    123 |    0.17        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                          2     0(0.00%) |     40       9      70      9 |    0.33        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                          4     0(0.00%) |     34       7      93     16 |    0.50        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          1     0(0.00%) |     97      97      97     97 |    0.17        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                          1     0(0.00%) |     97      97      97     97 |    0.17        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          1     0(0.00%) |     69      69      69     69 |    0.17        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                          2     0(0.00%) |     21      19      23     20 |    0.00        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                        79   15(18.99%) |     32       4     123     19 |    9.00        1.00

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                              7     0(0.00%) |     11       4      29      9 |    0.62        0.00
GET      /v1/leaderboard/streak                                                             7     0(0.00%) |      6       3      16      6 |    0.62        0.00
POST     /v1/quiz/answer                                                                   40   20(50.00%) |     20      11      89     17 |    3.38        1.25
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              1     0(0.00%) |     10      10      10     10 |    0.12        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              1   1(100.00%) |     24      24      24     24 |    0.12        0.12
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              2    1(50.00%) |     43      12      74     13 |    0.25        0.12
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              1     0(0.00%) |      7       7       7      7 |    0.12        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              1     0(0.00%) |     12      12      12     12 |    0.00        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.12        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          3     0(0.00%) |     44      18      92     23 |    0.25        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          3     0(0.00%) |     39      17      83     17 |    0.25        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                          3     0(0.00%) |     22      17      25     22 |    0.25        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          1     0(0.00%) |     87      87      87     87 |    0.12        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          1     0(0.00%) |     16      16      16     16 |    0.12        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          3     0(0.00%) |     40      20      61     41 |    0.25        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          1     0(0.00%) |    102     102     102    102 |    0.12        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          1     0(0.00%) |     37      37      37     37 |    0.12        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          3     0(0.00%) |     27      21      39     21 |    0.38        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                          2     0(0.00%) |     28      16      40     17 |    0.25        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          1     0(0.00%) |     34      34      34     34 |    0.12        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          2     0(0.00%) |     88      55     122     55 |    0.12        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                          2     0(0.00%) |     53      17      90     18 |    0.12        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          1     0(0.00%) |    123     123     123    123 |    0.12        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                          2     0(0.00%) |     40       9      70      9 |    0.25        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                          5     0(0.00%) |     30       7      93     16 |    0.50        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          1     0(0.00%) |     97      97      97     97 |    0.12        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                          1     0(0.00%) |     97      97      97     97 |    0.12        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          2     0(0.00%) |     40      11      69     11 |    0.12        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                          2     0(0.00%) |     21      19      23     20 |    0.25        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       101   22(21.78%) |     29       3     123     18 |    9.38        1.50

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             10     0(0.00%) |     12       4      29      9 |    0.50        0.00
GET      /v1/leaderboard/streak                                                            10     0(0.00%) |      6       3      16      4 |    0.50        0.00
POST     /v1/quiz/answer                                                                   52   26(50.00%) |     20      11      89     17 |    3.90        1.90
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              1     0(0.00%) |     10      10      10     10 |    0.10        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              1   1(100.00%) |     24      24      24     24 |    0.10        0.10
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              2    1(50.00%) |     43      12      74     13 |    0.20        0.10
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              1     0(0.00%) |      7       7       7      7 |    0.10        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              1     0(0.00%) |     12      12      12     12 |    0.10        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.10        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          3     0(0.00%) |     44      18      92     23 |    0.20        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          3     0(0.00%) |     39      17      83     17 |    0.30        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                          3     0(0.00%) |     22      17      25     22 |    0.30        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          2     0(0.00%) |     53      19      87     19 |    0.10        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          1     0(0.00%) |     16      16      16     16 |    0.10        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          3     0(0.00%) |     40      20      61     41 |    0.30        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          1     0(0.00%) |    102     102     102    102 |    0.10        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          1     0(0.00%) |     37      37      37     37 |    0.10        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          3     0(0.00%) |     27      21      39     21 |    0.30        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                          3     0(0.00%) |     25      16      40     19 |    0.20        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          1     0(0.00%) |     34      34      34     34 |    0.10        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          2     0(0.00%) |     88      55     122     55 |    0.20        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                          2     0(0.00%) |     53      17      90     18 |    0.20        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          1     0(0.00%) |    123     123     123    123 |    0.10        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                          3     0(0.00%) |     40       9      70     40 |    0.20        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                          5     0(0.00%) |     30       7      93     16 |    0.50        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          1     0(0.00%) |     97      97      97     97 |    0.10        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                          1     0(0.00%) |     97      97      97     97 |    0.10        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          2     0(0.00%) |     40      11      69     11 |    0.20        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                          3     0(0.00%) |     22      19      23     23 |    0.20        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       123   28(22.76%) |     27       3     123     18 |    9.50        2.10

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             11     0(0.00%) |     12       4      29     10 |    1.00        0.00
GET      /v1/leaderboard/streak                                                            11     0(0.00%) |      5       3      16      4 |    1.00        0.00
POST     /v1/quiz/answer                                                                   61   31(50.82%) |     20       8      89     17 |    5.20        2.60
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              1     0(0.00%) |     10      10      10     10 |    0.10        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              1   1(100.00%) |     24      24      24     24 |    0.00        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              2    1(50.00%) |     43      12      74     13 |    0.10        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              1     0(0.00%) |      7       7       7      7 |    0.10        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              1     0(0.00%) |     12      12      12     12 |    0.10        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.10        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          3     0(0.00%) |     44      18      92     23 |    0.20        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          4     0(0.00%) |     35      17      83     17 |    0.20        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                          3     0(0.00%) |     22      17      25     22 |    0.30        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          2     0(0.00%) |     53      19      87     19 |    0.20        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          2     0(0.00%) |     19      16      22     17 |    0.10        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          3     0(0.00%) |     40      20      61     41 |    0.30        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          2     0(0.00%) |     60      18     102     18 |    0.10        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          1     0(0.00%) |     37      37      37     37 |    0.00        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          3     0(0.00%) |     27      21      39     21 |    0.20        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                          3     0(0.00%) |     25      16      40     19 |    0.30        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          2     0(0.00%) |     27      19      34     20 |    0.10        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          2     0(0.00%) |     88      55     122     55 |    0.10        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                          3     0(0.00%) |     41      15      90     18 |    0.20        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          2     0(0.00%) |     74      24     123     25 |    0.00        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                          3     0(0.00%) |     40       9      70     40 |    0.10        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                          5     0(0.00%) |     30       7      93     16 |    0.50        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          1     0(0.00%) |     97      97      97     97 |    0.10        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                          2     0(0.00%) |     59      22      97     22 |    0.10        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          2     0(0.00%) |     40      11      69     11 |    0.10        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                          3     0(0.00%) |     22      19      23     23 |    0.30        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       141   33(23.40%) |     25       3     123     18 |   11.20        2.60

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             11     0(0.00%) |     12       4      29     10 |    0.90        0.00
GET      /v1/leaderboard/streak                                                            11     0(0.00%) |      5       3      16      4 |    0.90        0.00
POST     /v1/quiz/answer                                                                   70   36(51.43%) |     19       3      89     17 |    5.30        3.10
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              1     0(0.00%) |     10      10      10     10 |    0.10        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              1   1(100.00%) |     24      24      24     24 |    0.00        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              2    1(50.00%) |     43      12      74     13 |    0.00        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              1     0(0.00%) |      7       7       7      7 |    0.00        0.00
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                              1     0(0.00%) |     14      14      14     14 |    0.00        0.00
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              1     0(0.00%) |     18      18      18     18 |    0.00        0.00
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                              1     0(0.00%) |     15      15      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              1     0(0.00%) |     12      12      12     12 |    0.10        0.00
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              1     0(0.00%) |     13      13      13     13 |    0.00        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.10        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          4     0(0.00%) |     38      18      92     19 |    0.20        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          4     0(0.00%) |     35      17      83     17 |    0.30        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                          4     0(0.00%) |     21      17      25     19 |    0.20        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          2     0(0.00%) |     53      19      87     19 |    0.10        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          2     0(0.00%) |     19      16      22     17 |    0.10        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          4     0(0.00%) |     36      20      61     23 |    0.20        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          2     0(0.00%) |     60      18     102     18 |    0.10        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          1     0(0.00%) |     37      37      37     37 |    0.00        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          4     0(0.00%) |     25      20      39     21 |    0.20        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                          4     0(0.00%) |     24      16      40     19 |    0.20        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          2     0(0.00%) |     27      19      34     20 |    0.10        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          2     0(0.00%) |     88      55     122     55 |    0.10        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                          3     0(0.00%) |     41      15      90     18 |    0.20        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          2     0(0.00%) |     74      24     123     25 |    0.10        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                          3     0(0.00%) |     40       9      70     40 |    0.10        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                          5     0(0.00%) |     30       7      93     16 |    0.30        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          1     0(0.00%) |     97      97      97     97 |    0.00        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                          2     0(0.00%) |     59      22      97     22 |    0.10        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          2     0(0.00%) |     40      11      69     11 |    0.10        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                          3     0(0.00%) |     22      19      23     23 |    0.30        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       159   38(23.90%) |     24       3     123     18 |   10.40        3.10

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             18     0(0.00%) |     10       4      29      9 |    0.80        0.00
GET      /v1/leaderboard/streak                                                            18     0(0.00%) |      5       1      16      4 |    0.80        0.00
POST     /v1/quiz/answer                                                                   78   40(51.28%) |     19       3      89     17 |    5.00        3.10
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              1     0(0.00%) |     10      10      10     10 |    0.00        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              1   1(100.00%) |     24      24      24     24 |    0.00        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              2    1(50.00%) |     43      12      74     13 |    0.00        0.00
GET      /v1/quiz/metrics/6a2d92f5-2099-47d8-b962-0b222d649a4b                              1     0(0.00%) |     14      14      14     14 |    0.00        0.00
GET      /v1/quiz/metrics/72aa43fb-feef-48bb-a87f-bb964858454c                              1     0(0.00%) |      5       5       5      5 |    0.00        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              1     0(0.00%) |      7       7       7      7 |    0.00        0.00
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                              1     0(0.00%) |     14      14      14     14 |    0.10        0.00
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              2     0(0.00%) |     16      14      18     15 |    0.10        0.00
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                              1     0(0.00%) |     15      15      15     15 |    0.10        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              1     0(0.00%) |     12      12      12     12 |    0.10        0.00
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              1     0(0.00%) |     13      13      13     13 |    0.10        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.10        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          4     0(0.00%) |     38      18      92     19 |    0.20        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          4     0(0.00%) |     35      17      83     17 |    0.30        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                          4     0(0.00%) |     21      17      25     19 |    0.30        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          2     0(0.00%) |     53      19      87     19 |    0.10        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          2     0(0.00%) |     19      16      22     17 |    0.10        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          4     0(0.00%) |     36      20      61     23 |    0.30        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          2     0(0.00%) |     60      18     102     18 |    0.10        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          1     0(0.00%) |     37      37      37     37 |    0.00        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          4     0(0.00%) |     25      20      39     21 |    0.20        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                          5     0(0.00%) |     22      15      40     19 |    0.30        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          2     0(0.00%) |     27      19      34     20 |    0.10        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          2     0(0.00%) |     88      55     122     55 |    0.10        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                          3     0(0.00%) |     41      15      90     18 |    0.20        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          2     0(0.00%) |     74      24     123     25 |    0.10        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                          5     0(0.00%) |     29       9      70     14 |    0.10        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                          5     0(0.00%) |     30       7      93     16 |    0.20        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          2     0(0.00%) |     56      14      97     15 |    0.00        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                          3     0(0.00%) |     46      20      97     22 |    0.10        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          2     0(0.00%) |     40      11      69     11 |    0.10        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                          3     0(0.00%) |     22      19      23     23 |    0.30        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       189   42(22.22%) |     22       1     123     17 |   10.40        3.10

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             19     0(0.00%) |     10       4      29      9 |    1.20        0.00
GET      /v1/leaderboard/streak                                                            19     0(0.00%) |      4       1      16      4 |    1.20        0.00
POST     /v1/quiz/answer                                                                   91   45(49.45%) |     18       3      89     17 |    5.00        3.00
GET      /v1/quiz/metrics/10c3e51a-10e6-419e-8570-97a5e2e418f7                              1     0(0.00%) |     10      10      10     10 |    0.00        0.00
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              1     0(0.00%) |     10      10      10     10 |    0.00        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              1   1(100.00%) |     24      24      24     24 |    0.00        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              2    1(50.00%) |     43      12      74     13 |    0.00        0.00
GET      /v1/quiz/metrics/6a2d92f5-2099-47d8-b962-0b222d649a4b                              1     0(0.00%) |     14      14      14     14 |    0.10        0.00
GET      /v1/quiz/metrics/72aa43fb-feef-48bb-a87f-bb964858454c                              2     0(0.00%) |      8       5      12      5 |    0.10        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              1     0(0.00%) |      7       7       7      7 |    0.00        0.00
GET      /v1/quiz/metrics/95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                              1     0(0.00%) |     14      14      14     14 |    0.10        0.00
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              2     0(0.00%) |     16      14      18     15 |    0.20        0.00
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                              1     0(0.00%) |     15      15      15     15 |    0.10        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              1     0(0.00%) |     12      12      12     12 |    0.10        0.00
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              1     0(0.00%) |     13      13      13     13 |    0.10        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          4     0(0.00%) |     38      18      92     19 |    0.20        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          4     0(0.00%) |     35      17      83     17 |    0.20        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                          4     0(0.00%) |     21      17      25     19 |    0.20        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          3     0(0.00%) |     42      19      87     21 |    0.10        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          2     0(0.00%) |     19      16      22     17 |    0.10        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          4     0(0.00%) |     36      20      61     23 |    0.20        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          2     0(0.00%) |     60      18     102     18 |    0.10        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          2     0(0.00%) |     22       8      37      9 |    0.00        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          4     0(0.00%) |     25      20      39     21 |    0.10        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                          5     0(0.00%) |     22      15      40     19 |    0.30        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          2     0(0.00%) |     27      19      34     20 |    0.10        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          2     0(0.00%) |     88      55     122     55 |    0.10        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                          3     0(0.00%) |     41      15      90     18 |    0.20        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          2     0(0.00%) |     74      24     123     25 |    0.10        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                          5     0(0.00%) |     29       9      70     14 |    0.20        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                          5     0(0.00%) |     30       7      93     16 |    0.10        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          3     0(0.00%) |     42      14      97     16 |    0.10        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                          3     0(0.00%) |     46      20      97     22 |    0.20        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          3     0(0.00%) |     34      11      69     23 |    0.10        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                          3     0(0.00%) |     22      19      23     23 |    0.10        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       211   47(22.27%) |     21       1     123     17 |   11.00        3.00

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             20     0(0.00%) |     10       4      29      9 |    1.40        0.00
GET      /v1/leaderboard/streak                                                            20     0(0.00%) |      4       1      16      4 |    1.40        0.00
POST     /v1/quiz/answer                                                                  104   54(51.92%) |     18       3      89     17 |    4.90        2.50
GET      /v1/quiz/metrics/10c3e51a-10e6-419e-8570-97a5e2e418f7                              1     0(0.00%) |     10      10      10     10 |    0.10        0.00
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              1     0(0.00%) |     10      10      10     10 |    0.00        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              1   1(100.00%) |     24      24      24     24 |    0.00        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              2    1(50.00%) |     43      12      74     13 |    0.00        0.00
GET      /v1/quiz/metrics/6a2d92f5-2099-47d8-b962-0b222d649a4b                              1     0(0.00%) |     14      14      14     14 |    0.10        0.00
GET      /v1/quiz/metrics/72aa43fb-feef-48bb-a87f-bb964858454c                              2     0(0.00%) |      8       5      12      5 |    0.20        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              1     0(0.00%) |      7       7       7      7 |    0.00        0.00
GET      /v1/quiz/metrics/95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                              1     0(0.00%) |     16      16      16     16 |    0.10        0.00
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                              2     0(0.00%) |     10       6      14      6 |    0.10        0.00
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              2     0(0.00%) |     16      14      18     15 |    0.20        0.00
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                              1     0(0.00%) |     15      15      15     15 |    0.10        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              1     0(0.00%) |     12      12      12     12 |    0.00        0.00
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              1     0(0.00%) |     13      13      13     13 |    0.10        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          4     0(0.00%) |     38      18      92     19 |    0.20        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          4     0(0.00%) |     35      17      83     17 |    0.10        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                          6     0(0.00%) |     19      13      25     19 |    0.10        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          3     0(0.00%) |     42      19      87     21 |    0.20        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          2     0(0.00%) |     19      16      22     17 |    0.10        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          4     0(0.00%) |     36      20      61     23 |    0.10        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          3     0(0.00%) |     47      18     102     22 |    0.10        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          2     0(0.00%) |     22       8      37      9 |    0.10        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          4     0(0.00%) |     25      20      39     21 |    0.10        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                          5     0(0.00%) |     22      15      40     19 |    0.30        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          2     0(0.00%) |     27      19      34     20 |    0.10        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          2     0(0.00%) |     88      55     122     55 |    0.00        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                          4     0(0.00%) |     37      15      90     18 |    0.10        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          2     0(0.00%) |     74      24     123     25 |    0.10        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                          6     0(0.00%) |     27       9      70     14 |    0.30        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                          5     0(0.00%) |     30       7      93     16 |    0.00        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          3     0(0.00%) |     42      14      97     16 |    0.20        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                          3     0(0.00%) |     46      20      97     22 |    0.20        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          3     0(0.00%) |     34      11      69     23 |    0.10        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                          4     0(0.00%) |     22      19      23     22 |    0.10        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       233   56(24.03%) |     21       1     123     17 |   11.30        2.50

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             21     0(0.00%) |      9       4      29      9 |    1.00        0.00
GET      /v1/leaderboard/streak                                                            21     0(0.00%) |      4       1      16      4 |    1.00        0.00
POST     /v1/quiz/answer                                                                  115   63(54.78%) |     18       3      89     17 |    4.70        2.50
GET      /v1/quiz/metrics/10c3e51a-10e6-419e-8570-97a5e2e418f7                              1     0(0.00%) |     10      10      10     10 |    0.10        0.00
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              2     0(0.00%) |     11      10      11     11 |    0.00        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              1   1(100.00%) |     24      24      24     24 |    0.00        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              2    1(50.00%) |     43      12      74     13 |    0.00        0.00
GET      /v1/quiz/metrics/6a2d92f5-2099-47d8-b962-0b222d649a4b                              2     0(0.00%) |     14      14      15     15 |    0.10        0.00
GET      /v1/quiz/metrics/72aa43fb-feef-48bb-a87f-bb964858454c                              2     0(0.00%) |      8       5      12      5 |    0.20        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              1     0(0.00%) |      7       7       7      7 |    0.00        0.00
GET      /v1/quiz/metrics/95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                              1     0(0.00%) |     16      16      16     16 |    0.10        0.00
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                              2     0(0.00%) |     10       6      14      6 |    0.20        0.00
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              2     0(0.00%) |     16      14      18     15 |    0.20        0.00
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                              1     0(0.00%) |     15      15      15     15 |    0.10        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              1     0(0.00%) |     12      12      12     12 |    0.00        0.00
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              1     0(0.00%) |     13      13      13     13 |    0.10        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/eecb7e1c-adee-4807-8da7-d9a03326cc13                              1     0(0.00%) |     18      18      18     18 |    0.00        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          4     0(0.00%) |     38      18      92     19 |    0.10        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          4     0(0.00%) |     35      17      83     17 |    0.10        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                          6     0(0.00%) |     19      13      25     19 |    0.20        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          3     0(0.00%) |     42      19      87     21 |    0.10        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          2     0(0.00%) |     19      16      22     17 |    0.10        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          4     0(0.00%) |     36      20      61     23 |    0.10        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          3     0(0.00%) |     47      18     102     22 |    0.10        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          3     0(0.00%) |     19       8      37     13 |    0.10        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          6     0(0.00%) |     22      11      39     20 |    0.10        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                          5     0(0.00%) |     22      15      40     19 |    0.20        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          2     0(0.00%) |     27      19      34     20 |    0.10        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          2     0(0.00%) |     88      55     122     55 |    0.00        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                          5     0(0.00%) |     34      15      90     20 |    0.20        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          2     0(0.00%) |     74      24     123     25 |    0.10        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                          6     0(0.00%) |     27       9      70     14 |    0.40        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                          6     0(0.00%) |     29       7      93     16 |    0.00        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          3     0(0.00%) |     42      14      97     16 |    0.20        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                          4     0(0.00%) |     40      20      97     22 |    0.20        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          3     0(0.00%) |     34      11      69     23 |    0.10        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                          4     0(0.00%) |     22      19      23     22 |    0.10        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       255   65(25.49%) |     20       1     123     17 |   10.40        2.50

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             23     0(0.00%) |      9       4      29      9 |    1.00        0.00
GET      /v1/leaderboard/streak                                                            23     0(0.00%) |      4       1      16      4 |    1.00        0.00
POST     /v1/quiz/answer                                                                  124   68(54.84%) |     18       3      89     17 |    5.20        3.00
GET      /v1/quiz/metrics/10c3e51a-10e6-419e-8570-97a5e2e418f7                              1     0(0.00%) |     10      10      10     10 |    0.10        0.00
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              2     0(0.00%) |     11      10      11     11 |    0.10        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              1   1(100.00%) |     24      24      24     24 |    0.00        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              3    1(33.33%) |     31       8      74     13 |    0.00        0.00
GET      /v1/quiz/metrics/6a2d92f5-2099-47d8-b962-0b222d649a4b                              2     0(0.00%) |     14      14      15     15 |    0.20        0.00
GET      /v1/quiz/metrics/72aa43fb-feef-48bb-a87f-bb964858454c                              2     0(0.00%) |      8       5      12      5 |    0.20        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              1     0(0.00%) |      7       7       7      7 |    0.00        0.00
GET      /v1/quiz/metrics/95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                              1     0(0.00%) |     16      16      16     16 |    0.10        0.00
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                              2     0(0.00%) |     10       6      14      6 |    0.20        0.00
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              2     0(0.00%) |     16      14      18     15 |    0.20        0.00
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                              1     0(0.00%) |     15      15      15     15 |    0.10        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              1     0(0.00%) |     12      12      12     12 |    0.00        0.00
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              2     0(0.00%) |     14      13      15     13 |    0.10        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/eecb7e1c-adee-4807-8da7-d9a03326cc13                              1     0(0.00%) |     18      18      18     18 |    0.10        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          5     0(0.00%) |     34      18      92     19 |    0.10        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          5     0(0.00%) |     34      17      83     25 |    0.00        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                          7     0(0.00%) |     19      13      25     19 |    0.30        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          3     0(0.00%) |     42      19      87     21 |    0.10        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          2     0(0.00%) |     19      16      22     17 |    0.00        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          5     0(0.00%) |     32      14      61     23 |    0.10        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          3     0(0.00%) |     47      18     102     22 |    0.10        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          4     0(0.00%) |     17       8      37     11 |    0.20        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          6     0(0.00%) |     22      11      39     20 |    0.30        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                          5     0(0.00%) |     22      15      40     19 |    0.20        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          2     0(0.00%) |     27      19      34     20 |    0.00        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          2     0(0.00%) |     88      55     122     55 |    0.00        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                          5     0(0.00%) |     34      15      90     20 |    0.10        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          3     0(0.00%) |     53      10     123     25 |    0.00        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                          6     0(0.00%) |     27       9      70     14 |    0.30        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                          6     0(0.00%) |     29       7      93     16 |    0.10        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          4     0(0.00%) |     35      14      97     15 |    0.20        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                          4     0(0.00%) |     40      20      97     22 |    0.20        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          3     0(0.00%) |     34      11      69     23 |    0.10        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                          4     0(0.00%) |     22      19      23     22 |    0.10        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       277   70(25.27%) |     20       1     123     16 |   11.10        3.00

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             24     0(0.00%) |      9       2      29      9 |    1.10        0.00
GET      /v1/leaderboard/streak                                                            24     0(0.00%) |      4       1      16      4 |    1.10        0.00
POST     /v1/quiz/answer                                                                  131   71(54.20%) |     17       3      89     17 |    5.10        3.00
GET      /v1/quiz/metrics/10c3e51a-10e6-419e-8570-97a5e2e418f7                              2     0(0.00%) |      9       8      10      8 |    0.10        0.00
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              2     0(0.00%) |     11      10      11     11 |    0.10        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              2    1(50.00%) |     19      15      24     15 |    0.00        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              3    1(33.33%) |     31       8      74     13 |    0.10        0.00
GET      /v1/quiz/metrics/6a2d92f5-2099-47d8-b962-0b222d649a4b                              2     0(0.00%) |     14      14      15     15 |    0.20        0.00
GET      /v1/quiz/metrics/72aa43fb-feef-48bb-a87f-bb964858454c                              2     0(0.00%) |      8       5      12      5 |    0.20        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              1     0(0.00%) |      7       7       7      7 |    0.00        0.00
GET      /v1/quiz/metrics/95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                              1     0(0.00%) |     16      16      16     16 |    0.10        0.00
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                              2     0(0.00%) |     10       6      14      6 |    0.10        0.00
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              2     0(0.00%) |     16      14      18     15 |    0.10        0.00
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                              1     0(0.00%) |     15      15      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/bfe4a522-1c93-40fd-bb19-aba9aca034fd                              1     0(0.00%) |      6       6       6      6 |    0.00        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              1     0(0.00%) |     12      12      12     12 |    0.00        0.00
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              2     0(0.00%) |     14      13      15     13 |    0.10        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/eecb7e1c-adee-4807-8da7-d9a03326cc13                              1     0(0.00%) |     18      18      18     18 |    0.10        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          5     0(0.00%) |     34      18      92     19 |    0.10        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          5     0(0.00%) |     34      17      83     25 |    0.00        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                          7     0(0.00%) |     19      13      25     19 |    0.30        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          4     0(0.00%) |     35      14      87     19 |    0.10        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          2     0(0.00%) |     19      16      22     17 |    0.00        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          5     0(0.00%) |     32      14      61     23 |    0.10        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          3     0(0.00%) |     47      18     102     22 |    0.10        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          5     0(0.00%) |     16       8      37     13 |    0.30        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          6     0(0.00%) |     22      11      39     20 |    0.20        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                          6     0(0.00%) |     22      15      40     19 |    0.10        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          2     0(0.00%) |     27      19      34     20 |    0.00        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          3     0(0.00%) |     65      19     122     55 |    0.00        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                          5     0(0.00%) |     34      15      90     20 |    0.20        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          3     0(0.00%) |     53      10     123     25 |    0.10        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                          6     0(0.00%) |     27       9      70     14 |    0.30        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                          6     0(0.00%) |     29       7      93     16 |    0.10        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          4     0(0.00%) |     35      14      97     15 |    0.20        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                          4     0(0.00%) |     40      20      97     22 |    0.20        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          3     0(0.00%) |     34      11      69     23 |    0.10        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                          5     0(0.00%) |     21      19      23     22 |    0.10        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       294   73(24.83%) |     19       1     123     16 |   11.10        3.00

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             25     0(0.00%) |      9       2      29      9 |    0.70        0.00
GET      /v1/leaderboard/streak                                                            25     0(0.00%) |      4       1      16      4 |    0.70        0.00
POST     /v1/quiz/answer                                                                  143   79(55.24%) |     18       3      89     17 |    5.30        3.10
GET      /v1/quiz/metrics/10c3e51a-10e6-419e-8570-97a5e2e418f7                              3     0(0.00%) |     10       8      12     11 |    0.20        0.00
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              2     0(0.00%) |     11      10      11     11 |    0.10        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              2    1(50.00%) |     19      15      24     15 |    0.10        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              3    1(33.33%) |     31       8      74     13 |    0.10        0.00
GET      /v1/quiz/metrics/6a2d92f5-2099-47d8-b962-0b222d649a4b                              2     0(0.00%) |     14      14      15     15 |    0.10        0.00
GET      /v1/quiz/metrics/7252045d-4936-45a3-b06a-71ef15fdde83                              1     0(0.00%) |      8       8       8      8 |    0.00        0.00
GET      /v1/quiz/metrics/72aa43fb-feef-48bb-a87f-bb964858454c                              2     0(0.00%) |      8       5      12      5 |    0.10        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              1     0(0.00%) |      7       7       7      7 |    0.00        0.00
GET      /v1/quiz/metrics/95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                              1     0(0.00%) |     16      16      16     16 |    0.10        0.00
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                              2     0(0.00%) |     10       6      14      6 |    0.10        0.00
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              2     0(0.00%) |     16      14      18     15 |    0.00        0.00
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                              1     0(0.00%) |     15      15      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/bfe4a522-1c93-40fd-bb19-aba9aca034fd                              2     0(0.00%) |      6       6       7      6 |    0.10        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              1     0(0.00%) |     12      12      12     12 |    0.00        0.00
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              2     0(0.00%) |     14      13      15     13 |    0.10        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/eecb7e1c-adee-4807-8da7-d9a03326cc13                              1     0(0.00%) |     18      18      18     18 |    0.10        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          5     0(0.00%) |     34      18      92     19 |    0.10        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          5     0(0.00%) |     34      17      83     25 |    0.10        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                          8     0(0.00%) |     19      13      25     19 |    0.30        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          5     0(0.00%) |     32      14      87     19 |    0.20        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          2     0(0.00%) |     19      16      22     17 |    0.00        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          5     0(0.00%) |     32      14      61     23 |    0.10        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          3     0(0.00%) |     47      18     102     22 |    0.10        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          5     0(0.00%) |     16       8      37     13 |    0.40        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          6     0(0.00%) |     22      11      39     20 |    0.20        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                          6     0(0.00%) |     22      15      40     19 |    0.00        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          2     0(0.00%) |     27      19      34     20 |    0.00        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          4     0(0.00%) |     53      18     122     20 |    0.10        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                          5     0(0.00%) |     34      15      90     20 |    0.20        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          3     0(0.00%) |     53      10     123     25 |    0.10        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                          6     0(0.00%) |     27       9      70     14 |    0.20        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                          6     0(0.00%) |     29       7      93     16 |    0.10        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          4     0(0.00%) |     35      14      97     15 |    0.20        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                          5     0(0.00%) |     37      20      97     22 |    0.10        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          4     0(0.00%) |     33      11      69     23 |    0.10        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                          5     0(0.00%) |     21      19      23     22 |    0.20        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       316   81(25.63%) |     19       1     123     16 |   10.70        3.10

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             28     0(0.00%) |      9       2      29      9 |    0.60        0.00
GET      /v1/leaderboard/streak                                                            28     0(0.00%) |      4       1      16      4 |    0.60        0.00
POST     /v1/quiz/answer                                                                  148   81(54.73%) |     18       3      89     17 |    5.30        3.50
GET      /v1/quiz/metrics/10c3e51a-10e6-419e-8570-97a5e2e418f7                              3     0(0.00%) |     10       8      12     11 |    0.20        0.00
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              3     0(0.00%) |     13      10      19     12 |    0.10        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              2    1(50.00%) |     19      15      24     15 |    0.10        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              3    1(33.33%) |     31       8      74     13 |    0.10        0.00
GET      /v1/quiz/metrics/6a2d92f5-2099-47d8-b962-0b222d649a4b                              2     0(0.00%) |     14      14      15     15 |    0.10        0.00
GET      /v1/quiz/metrics/7252045d-4936-45a3-b06a-71ef15fdde83                              1     0(0.00%) |      8       8       8      8 |    0.10        0.00
GET      /v1/quiz/metrics/72aa43fb-feef-48bb-a87f-bb964858454c                              2     0(0.00%) |      8       5      12      5 |    0.00        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              1     0(0.00%) |      7       7       7      7 |    0.00        0.00
GET      /v1/quiz/metrics/95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                              2     0(0.00%) |     10       6      14      6 |    0.10        0.00
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              2     0(0.00%) |     16      14      18     15 |    0.00        0.00
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                              1     0(0.00%) |     15      15      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/bfe4a522-1c93-40fd-bb19-aba9aca034fd                              2     0(0.00%) |      6       6       7      6 |    0.20        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              2     0(0.00%) |     11      10      12     10 |    0.00        0.00
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              2     0(0.00%) |     14      13      15     13 |    0.10        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/eecb7e1c-adee-4807-8da7-d9a03326cc13                              1     0(0.00%) |     18      18      18     18 |    0.10        0.00
GET      /v1/quiz/metrics/f45f9a26-8ac6-4fe1-83b1-98538770e29c                              1     0(0.00%) |     14      14      14     14 |    0.00        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          6     0(0.00%) |     32      18      92     19 |    0.10        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          6     0(0.00%) |     31      15      83     17 |    0.10        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                          8     0(0.00%) |     19      13      25     19 |    0.40        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          5     0(0.00%) |     32      14      87     19 |    0.20        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          3     0(0.00%) |     22      16      29     23 |    0.00        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          5     0(0.00%) |     32      14      61     23 |    0.10        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          3     0(0.00%) |     47      18     102     22 |    0.10        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          6     0(0.00%) |     16       8      37     13 |    0.30        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          6     0(0.00%) |     22      11      39     20 |    0.20        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                          6     0(0.00%) |     22      15      40     19 |    0.10        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          3     0(0.00%) |     22      14      34     20 |    0.00        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          4     0(0.00%) |     53      18     122     20 |    0.20        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                          6     0(0.00%) |     31      15      90     18 |    0.20        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          4     0(0.00%) |     43      10     123     15 |    0.10        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                          6     0(0.00%) |     27       9      70     14 |    0.10        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                          7     0(0.00%) |     27       7      93     19 |    0.10        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          6     0(0.00%) |     32      14      97     16 |    0.10        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                          5     0(0.00%) |     37      20      97     22 |    0.20        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          5     0(0.00%) |     31      11      69     23 |    0.00        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                          5     0(0.00%) |     21      19      23     22 |    0.20        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       341   83(24.34%) |     19       1     123     16 |   10.50        3.50

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             31     0(0.00%) |      9       2      29      8 |    0.70        0.00
GET      /v1/leaderboard/streak                                                            31     0(0.00%) |      4       1      16      4 |    0.70        0.00
POST     /v1/quiz/answer                                                                  154   84(54.55%) |     18       3      89     16 |    4.70        3.00
GET      /v1/quiz/metrics/10c3e51a-10e6-419e-8570-97a5e2e418f7                              3     0(0.00%) |     10       8      12     11 |    0.20        0.00
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              3     0(0.00%) |     13      10      19     12 |    0.10        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              2    1(50.00%) |     19      15      24     15 |    0.10        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              4    1(25.00%) |     26       8      74     10 |    0.10        0.00
GET      /v1/quiz/metrics/6a2d92f5-2099-47d8-b962-0b222d649a4b                              2     0(0.00%) |     14      14      15     15 |    0.10        0.00
GET      /v1/quiz/metrics/7252045d-4936-45a3-b06a-71ef15fdde83                              1     0(0.00%) |      8       8       8      8 |    0.10        0.00
GET      /v1/quiz/metrics/72aa43fb-feef-48bb-a87f-bb964858454c                              2     0(0.00%) |      8       5      12      5 |    0.00        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              1     0(0.00%) |      7       7       7      7 |    0.00        0.00
GET      /v1/quiz/metrics/95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                              2     0(0.00%) |     10       6      14      6 |    0.00        0.00
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              2     0(0.00%) |     16      14      18     15 |    0.00        0.00
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                              1     0(0.00%) |     15      15      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/bfe4a522-1c93-40fd-bb19-aba9aca034fd                              2     0(0.00%) |      6       6       7      6 |    0.20        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              2     0(0.00%) |     11      10      12     10 |    0.10        0.00
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              2     0(0.00%) |     14      13      15     13 |    0.10        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/eecb7e1c-adee-4807-8da7-d9a03326cc13                              1     0(0.00%) |     18      18      18     18 |    0.10        0.00
GET      /v1/quiz/metrics/f45f9a26-8ac6-4fe1-83b1-98538770e29c                              3     0(0.00%) |     13      12      14     14 |    0.10        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          6     0(0.00%) |     32      18      92     19 |    0.10        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          6     0(0.00%) |     31      15      83     17 |    0.20        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                          8     0(0.00%) |     19      13      25     19 |    0.30        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          5     0(0.00%) |     32      14      87     19 |    0.20        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          4     0(0.00%) |     22      16      29     22 |    0.10        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          5     0(0.00%) |     32      14      61     23 |    0.10        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          4     0(0.00%) |     41      18     102     22 |    0.10        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          6     0(0.00%) |     16       8      37     13 |    0.40        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          6     0(0.00%) |     22      11      39     20 |    0.20        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                          7     0(0.00%) |     22      15      40     21 |    0.10        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          3     0(0.00%) |     22      14      34     20 |    0.10        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          4     0(0.00%) |     53      18     122     20 |    0.20        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                          7     0(0.00%) |     29      15      90     18 |    0.20        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          5     0(0.00%) |     37      10     123     15 |    0.20        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                          7     0(0.00%) |     25       9      70     15 |    0.00        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                          7     0(0.00%) |     27       7      93     19 |    0.10        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          7     0(0.00%) |     29      13      97     16 |    0.30        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                          6     0(0.00%) |     34      20      97     22 |    0.20        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          5     0(0.00%) |     31      11      69     23 |    0.20        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                          5     0(0.00%) |     21      19      23     22 |    0.10        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       364   86(23.63%) |     19       1     123     16 |   10.80        3.00

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             33     0(0.00%) |     17       2     272      9 |    1.00        0.00
GET      /v1/leaderboard/streak                                                            33     0(0.00%) |      4       1      16      4 |    1.00        0.00
POST     /v1/quiz/answer                                                                  160   86(53.75%) |     18       3      89     17 |    3.90        2.20
GET      /v1/quiz/metrics/10c3e51a-10e6-419e-8570-97a5e2e418f7                              3     0(0.00%) |     10       8      12     11 |    0.20        0.00
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              3     0(0.00%) |     13      10      19     12 |    0.10        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              2    1(50.00%) |     19      15      24     15 |    0.10        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              4    1(25.00%) |     26       8      74     10 |    0.10        0.00
GET      /v1/quiz/metrics/6a2d92f5-2099-47d8-b962-0b222d649a4b                              2     0(0.00%) |     14      14      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/7252045d-4936-45a3-b06a-71ef15fdde83                              1     0(0.00%) |      8       8       8      8 |    0.10        0.00
GET      /v1/quiz/metrics/72aa43fb-feef-48bb-a87f-bb964858454c                              2     0(0.00%) |      8       5      12      5 |    0.00        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              1     0(0.00%) |      7       7       7      7 |    0.00        0.00
GET      /v1/quiz/metrics/95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                              3     0(0.00%) |     77       6     210     15 |    0.00        0.00
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              2     0(0.00%) |     16      14      18     15 |    0.00        0.00
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                              1     0(0.00%) |     15      15      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/bfe4a522-1c93-40fd-bb19-aba9aca034fd                              3     0(0.00%) |     15       6      32      8 |    0.20        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              2     0(0.00%) |     11      10      12     10 |    0.10        0.00
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              2     0(0.00%) |     14      13      15     13 |    0.10        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/eecb7e1c-adee-4807-8da7-d9a03326cc13                              1     0(0.00%) |     18      18      18     18 |    0.00        0.00
GET      /v1/quiz/metrics/f45f9a26-8ac6-4fe1-83b1-98538770e29c                              3     0(0.00%) |     13      12      14     14 |    0.20        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          6     0(0.00%) |     32      18      92     19 |    0.20        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          6     0(0.00%) |     31      15      83     17 |    0.20        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                          9     0(0.00%) |     18      13      25     19 |    0.20        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          5     0(0.00%) |     32      14      87     19 |    0.20        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          4     0(0.00%) |     22      16      29     22 |    0.20        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          6     0(0.00%) |     31      14      61     23 |    0.10        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          4     0(0.00%) |     41      18     102     22 |    0.10        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          7     0(0.00%) |     16       8      37     14 |    0.30        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          6     0(0.00%) |     22      11      39     20 |    0.00        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                          7     0(0.00%) |     22      15      40     21 |    0.10        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          3     0(0.00%) |     22      14      34     20 |    0.10        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          4     0(0.00%) |     53      18     122     20 |    0.20        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                          8     0(0.00%) |     27      14      90     18 |    0.30        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          5     0(0.00%) |     37      10     123     15 |    0.30        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                          7     0(0.00%) |     25       9      70     15 |    0.10        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                          7     0(0.00%) |     27       7      93     19 |    0.10        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          7     0(0.00%) |     29      13      97     16 |    0.40        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                          6     0(0.00%) |     34      20      97     22 |    0.20        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          5     0(0.00%) |     31      11      69     23 |    0.20        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                          6     0(0.00%) |     22      19      23     22 |    0.10        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       381   88(23.10%) |     20       1     272     16 |   10.70        2.20

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             36     0(0.00%) |     16       2     272      9 |    1.10        0.00
GET      /v1/leaderboard/streak                                                            36     0(0.00%) |      4       1      16      4 |    1.00        0.00
POST     /v1/quiz/answer                                                                  170   90(52.94%) |     20       3     168     17 |    3.90        2.00
GET      /v1/quiz/metrics/10c3e51a-10e6-419e-8570-97a5e2e418f7                              3     0(0.00%) |     10       8      12     11 |    0.20        0.00
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              3     0(0.00%) |     13      10      19     12 |    0.10        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              2    1(50.00%) |     19      15      24     15 |    0.10        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              4    1(25.00%) |     26       8      74     10 |    0.10        0.00
GET      /v1/quiz/metrics/6a2d92f5-2099-47d8-b962-0b222d649a4b                              2     0(0.00%) |     14      14      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/7252045d-4936-45a3-b06a-71ef15fdde83                              1     0(0.00%) |      8       8       8      8 |    0.10        0.00
GET      /v1/quiz/metrics/72aa43fb-feef-48bb-a87f-bb964858454c                              2     0(0.00%) |      8       5      12      5 |    0.00        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              1     0(0.00%) |      7       7       7      7 |    0.00        0.00
GET      /v1/quiz/metrics/95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                              3     0(0.00%) |     77       6     210     15 |    0.10        0.00
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              2     0(0.00%) |     16      14      18     15 |    0.00        0.00
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                              1     0(0.00%) |     15      15      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/bfe4a522-1c93-40fd-bb19-aba9aca034fd                              3     0(0.00%) |     15       6      32      8 |    0.30        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              2     0(0.00%) |     11      10      12     10 |    0.10        0.00
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              2     0(0.00%) |     14      13      15     13 |    0.00        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/eecb7e1c-adee-4807-8da7-d9a03326cc13                              1     0(0.00%) |     18      18      18     18 |    0.00        0.00
GET      /v1/quiz/metrics/f45f9a26-8ac6-4fe1-83b1-98538770e29c                              3     0(0.00%) |     13      12      14     14 |    0.30        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          7     0(0.00%) |     62      18     244     22 |    0.10        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          7     0(0.00%) |     61      15     242     25 |    0.20        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                          9     0(0.00%) |     18      13      25     19 |    0.20        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          5     0(0.00%) |     32      14      87     19 |    0.20        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          4     0(0.00%) |     22      16      29     22 |    0.20        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          6     0(0.00%) |     31      14      61     23 |    0.10        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          4     0(0.00%) |     41      18     102     22 |    0.10        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          7     0(0.00%) |     16       8      37     14 |    0.30        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          7     0(0.00%) |     26      11      50     21 |    0.00        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                          7     0(0.00%) |     22      15      40     21 |    0.20        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          3     0(0.00%) |     22      14      34     20 |    0.10        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          5     0(0.00%) |     46      17     122     20 |    0.20        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                          8     0(0.00%) |     27      14      90     18 |    0.30        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          6     0(0.00%) |     36      10     123     15 |    0.20        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                          7     0(0.00%) |     25       9      70     15 |    0.10        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                          7     0(0.00%) |     27       7      93     19 |    0.10        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          8     0(0.00%) |     28      13      97     16 |    0.40        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                          7     0(0.00%) |     53      20     168     22 |    0.20        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          6     0(0.00%) |     66      11     244     23 |    0.20        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                          7     0(0.00%) |     39      19     141     22 |    0.20        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       406   92(22.66%) |     23       1     272     16 |   11.00        2.00

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             40     0(0.00%) |     15       2     272      8 |    1.00        0.00
GET      /v1/leaderboard/streak                                                            40     0(0.00%) |      4       1      16      4 |    1.00        0.00
POST     /v1/quiz/answer                                                                  178   93(52.25%) |     20       3     168     17 |    3.80        1.80
GET      /v1/quiz/metrics/10c3e51a-10e6-419e-8570-97a5e2e418f7                              3     0(0.00%) |     10       8      12     11 |    0.10        0.00
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              4     0(0.00%) |     14      10      19     12 |    0.10        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              2    1(50.00%) |     19      15      24     15 |    0.00        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              5    1(20.00%) |     23       8      74     11 |    0.10        0.00
GET      /v1/quiz/metrics/6a2d92f5-2099-47d8-b962-0b222d649a4b                              2     0(0.00%) |     14      14      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/7252045d-4936-45a3-b06a-71ef15fdde83                              1     0(0.00%) |      8       8       8      8 |    0.10        0.00
GET      /v1/quiz/metrics/72aa43fb-feef-48bb-a87f-bb964858454c                              2     0(0.00%) |      8       5      12      5 |    0.00        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              1     0(0.00%) |      7       7       7      7 |    0.00        0.00
GET      /v1/quiz/metrics/95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                              3     0(0.00%) |     77       6     210     15 |    0.10        0.00
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              2     0(0.00%) |     16      14      18     15 |    0.00        0.00
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                              1     0(0.00%) |     15      15      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/bfe4a522-1c93-40fd-bb19-aba9aca034fd                              3     0(0.00%) |     15       6      32      8 |    0.20        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              2     0(0.00%) |     11      10      12     10 |    0.10        0.00
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              2     0(0.00%) |     14      13      15     13 |    0.00        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/eecb7e1c-adee-4807-8da7-d9a03326cc13                              1     0(0.00%) |     18      18      18     18 |    0.00        0.00
GET      /v1/quiz/metrics/f45f9a26-8ac6-4fe1-83b1-98538770e29c                              3     0(0.00%) |     13      12      14     14 |    0.30        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          7     0(0.00%) |     62      18     244     22 |    0.20        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          7     0(0.00%) |     61      15     242     25 |    0.20        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                          9     0(0.00%) |     18      13      25     19 |    0.20        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          5     0(0.00%) |     32      14      87     19 |    0.10        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          4     0(0.00%) |     22      16      29     22 |    0.20        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          6     0(0.00%) |     31      14      61     23 |    0.10        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          5     0(0.00%) |     36      18     102     22 |    0.10        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          7     0(0.00%) |     16       8      37     14 |    0.20        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          7     0(0.00%) |     26      11      50     21 |    0.10        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                          8     0(0.00%) |     21      15      40     20 |    0.20        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          4     0(0.00%) |     22      14      34     20 |    0.10        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          5     0(0.00%) |     46      17     122     20 |    0.20        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                          8     0(0.00%) |     27      14      90     18 |    0.30        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          6     0(0.00%) |     36      10     123     15 |    0.30        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                          7     0(0.00%) |     25       9      70     15 |    0.10        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                          8     0(0.00%) |     27       7      93     19 |    0.10        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          8     0(0.00%) |     28      13      97     16 |    0.40        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                          8     0(0.00%) |     49      20     168     22 |    0.30        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          6     0(0.00%) |     66      11     244     23 |    0.30        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                          8     0(0.00%) |     36      18     141     22 |    0.20        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       430   95(22.09%) |     22       1     272     16 |   10.80        1.80

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             40     0(0.00%) |     15       2     272      8 |    1.50        0.00
GET      /v1/leaderboard/streak                                                            40     0(0.00%) |      4       1      16      4 |    1.50        0.00
POST     /v1/quiz/answer                                                                  191  101(52.88%) |     19       3     168     17 |    3.50        1.30
GET      /v1/quiz/metrics/10c3e51a-10e6-419e-8570-97a5e2e418f7                              3     0(0.00%) |     10       8      12     11 |    0.00        0.00
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              4     0(0.00%) |     14      10      19     12 |    0.20        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              2    1(50.00%) |     19      15      24     15 |    0.00        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              5    1(20.00%) |     23       8      74     11 |    0.20        0.00
GET      /v1/quiz/metrics/6a2d92f5-2099-47d8-b962-0b222d649a4b                              2     0(0.00%) |     14      14      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/7252045d-4936-45a3-b06a-71ef15fdde83                              1     0(0.00%) |      8       8       8      8 |    0.00        0.00
GET      /v1/quiz/metrics/72aa43fb-feef-48bb-a87f-bb964858454c                              2     0(0.00%) |      8       5      12      5 |    0.00        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              1     0(0.00%) |      7       7       7      7 |    0.00        0.00
GET      /v1/quiz/metrics/95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                              3     0(0.00%) |     77       6     210     15 |    0.10        0.00
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              2     0(0.00%) |     16      14      18     15 |    0.00        0.00
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                              1     0(0.00%) |     15      15      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/bfe4a522-1c93-40fd-bb19-aba9aca034fd                              3     0(0.00%) |     15       6      32      8 |    0.10        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              2     0(0.00%) |     11      10      12     10 |    0.10        0.00
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              2     0(0.00%) |     14      13      15     13 |    0.00        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/eecb7e1c-adee-4807-8da7-d9a03326cc13                              1     0(0.00%) |     18      18      18     18 |    0.00        0.00
GET      /v1/quiz/metrics/f45f9a26-8ac6-4fe1-83b1-98538770e29c                              3     0(0.00%) |     13      12      14     14 |    0.30        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          7     0(0.00%) |     62      18     244     22 |    0.20        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          7     0(0.00%) |     61      15     242     25 |    0.20        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                         10     0(0.00%) |     19      13      25     19 |    0.10        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          5     0(0.00%) |     32      14      87     19 |    0.00        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          4     0(0.00%) |     22      16      29     22 |    0.20        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          6     0(0.00%) |     31      14      61     23 |    0.10        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          6     0(0.00%) |     33      15     102     19 |    0.20        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          7     0(0.00%) |     16       8      37     14 |    0.20        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          8     0(0.00%) |     25      11      50     20 |    0.10        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                          9     0(0.00%) |     21      15      40     20 |    0.20        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          4     0(0.00%) |     22      14      34     20 |    0.10        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          6     0(0.00%) |     42      17     122     20 |    0.10        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                          8     0(0.00%) |     27      14      90     18 |    0.30        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          6     0(0.00%) |     36      10     123     15 |    0.30        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                          7     0(0.00%) |     25       9      70     15 |    0.10        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                          9     0(0.00%) |     27       7      93     22 |    0.20        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          9     0(0.00%) |     27      13      97     16 |    0.40        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                          9     0(0.00%) |     46      20     168     22 |    0.30        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          6     0(0.00%) |     66      11     244     23 |    0.30        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                          8     0(0.00%) |     36      18     141     22 |    0.20        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       451  103(22.84%) |     22       1     272     16 |   11.30        1.30

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             41     0(0.00%) |     15       2     272      9 |    1.30        0.00
GET      /v1/leaderboard/streak                                                            41     0(0.00%) |      4       1      16      4 |    1.30        0.00
POST     /v1/quiz/answer                                                                  195  104(53.33%) |     19       3     168     17 |    4.00        1.60
GET      /v1/quiz/metrics/10c3e51a-10e6-419e-8570-97a5e2e418f7                              3     0(0.00%) |     10       8      12     11 |    0.00        0.00
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              4     0(0.00%) |     14      10      19     12 |    0.20        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              2    1(50.00%) |     19      15      24     15 |    0.00        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              5    1(20.00%) |     23       8      74     11 |    0.20        0.00
GET      /v1/quiz/metrics/6a2d92f5-2099-47d8-b962-0b222d649a4b                              3     0(0.00%) |     13      10      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/7252045d-4936-45a3-b06a-71ef15fdde83                              1     0(0.00%) |      8       8       8      8 |    0.00        0.00
GET      /v1/quiz/metrics/72aa43fb-feef-48bb-a87f-bb964858454c                              2     0(0.00%) |      8       5      12      5 |    0.00        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              1     0(0.00%) |      7       7       7      7 |    0.00        0.00
GET      /v1/quiz/metrics/95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                              3     0(0.00%) |     77       6     210     15 |    0.10        0.00
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              2     0(0.00%) |     16      14      18     15 |    0.00        0.00
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                              1     0(0.00%) |     15      15      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/bfe4a522-1c93-40fd-bb19-aba9aca034fd                              3     0(0.00%) |     15       6      32      8 |    0.10        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              2     0(0.00%) |     11      10      12     10 |    0.00        0.00
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              2     0(0.00%) |     14      13      15     13 |    0.00        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/eecb7e1c-adee-4807-8da7-d9a03326cc13                              1     0(0.00%) |     18      18      18     18 |    0.00        0.00
GET      /v1/quiz/metrics/f45f9a26-8ac6-4fe1-83b1-98538770e29c                              4     0(0.00%) |     14      12      16     14 |    0.20        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          7     0(0.00%) |     62      18     244     22 |    0.20        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          7     0(0.00%) |     61      15     242     25 |    0.10        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                         11     0(0.00%) |     19      13      25     19 |    0.10        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          6     0(0.00%) |     28      12      87     19 |    0.00        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          4     0(0.00%) |     22      16      29     22 |    0.10        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          7     0(0.00%) |     30      14      61     23 |    0.10        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          6     0(0.00%) |     33      15     102     19 |    0.20        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          7     0(0.00%) |     16       8      37     14 |    0.10        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          9     0(0.00%) |     24      11      50     21 |    0.20        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                         10     0(0.00%) |     21      15      40     20 |    0.30        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          4     0(0.00%) |     22      14      34     20 |    0.10        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          7     0(0.00%) |     38      14     122     20 |    0.20        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                          9     0(0.00%) |     26      14      90     18 |    0.20        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          6     0(0.00%) |     36      10     123     15 |    0.20        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                          9     0(0.00%) |     24       9      70     19 |    0.10        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                          9     0(0.00%) |     27       7      93     22 |    0.30        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          9     0(0.00%) |     27      13      97     16 |    0.20        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                         10     0(0.00%) |     43      17     168     22 |    0.40        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          6     0(0.00%) |     66      11     244     23 |    0.10        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                          8     0(0.00%) |     36      18     141     22 |    0.30        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       469  106(22.60%) |     22       1     272     16 |   10.90        1.60

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             42     0(0.00%) |     15       2     272      9 |    1.10        0.00
GET      /v1/leaderboard/streak                                                            42     0(0.00%) |      4       1      16      4 |    1.10        0.00
POST     /v1/quiz/answer                                                                  202  109(53.96%) |     19       3     168     17 |    4.30        2.10
GET      /v1/quiz/metrics/10c3e51a-10e6-419e-8570-97a5e2e418f7                              3     0(0.00%) |     10       8      12     11 |    0.00        0.00
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              5     0(0.00%) |     13      10      19     13 |    0.10        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              2    1(50.00%) |     19      15      24     15 |    0.00        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              5    1(20.00%) |     23       8      74     11 |    0.20        0.00
GET      /v1/quiz/metrics/6a2d92f5-2099-47d8-b962-0b222d649a4b                              3     0(0.00%) |     13      10      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/7252045d-4936-45a3-b06a-71ef15fdde83                              1     0(0.00%) |      8       8       8      8 |    0.00        0.00
GET      /v1/quiz/metrics/72aa43fb-feef-48bb-a87f-bb964858454c                              2     0(0.00%) |      8       5      12      5 |    0.00        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              2     0(0.00%) |     10       7      12      7 |    0.00        0.00
GET      /v1/quiz/metrics/95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                              3     0(0.00%) |     77       6     210     15 |    0.10        0.00
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              2     0(0.00%) |     16      14      18     15 |    0.00        0.00
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                              1     0(0.00%) |     15      15      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/bfe4a522-1c93-40fd-bb19-aba9aca034fd                              3     0(0.00%) |     15       6      32      8 |    0.10        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              2     0(0.00%) |     11      10      12     10 |    0.00        0.00
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              3     0(0.00%) |     13      11      15     13 |    0.00        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/eecb7e1c-adee-4807-8da7-d9a03326cc13                              1     0(0.00%) |     18      18      18     18 |    0.00        0.00
GET      /v1/quiz/metrics/f45f9a26-8ac6-4fe1-83b1-98538770e29c                              4     0(0.00%) |     14      12      16     14 |    0.20        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          8     0(0.00%) |     57      18     244     21 |    0.10        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          7     0(0.00%) |     61      15     242     25 |    0.10        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                         11     0(0.00%) |     19      13      25     19 |    0.20        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          6     0(0.00%) |     28      12      87     19 |    0.10        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          5     0(0.00%) |     22      16      29     22 |    0.00        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          8     0(0.00%) |     29      14      61     23 |    0.20        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          6     0(0.00%) |     33      15     102     19 |    0.20        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          7     0(0.00%) |     16       8      37     14 |    0.10        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          9     0(0.00%) |     24      11      50     21 |    0.30        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                         10     0(0.00%) |     21      15      40     20 |    0.40        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          4     0(0.00%) |     22      14      34     20 |    0.10        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          8     0(0.00%) |     35      14     122     19 |    0.30        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                          9     0(0.00%) |     26      14      90     18 |    0.20        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          7     0(0.00%) |     34      10     123     22 |    0.10        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                          9     0(0.00%) |     24       9      70     19 |    0.10        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                          9     0(0.00%) |     27       7      93     22 |    0.20        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          9     0(0.00%) |     27      13      97     16 |    0.20        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                         10     0(0.00%) |     43      17     168     22 |    0.40        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          6     0(0.00%) |     66      11     244     23 |    0.10        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                          8     0(0.00%) |     36      18     141     22 |    0.30        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       486  111(22.84%) |     22       1     272     16 |   10.90        2.10

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             43     0(0.00%) |     15       2     272      9 |    0.90        0.00
GET      /v1/leaderboard/streak                                                            43     0(0.00%) |      4       1      16      4 |    1.00        0.00
POST     /v1/quiz/answer                                                                  211  111(52.61%) |     19       3     168     17 |    4.20        2.30
GET      /v1/quiz/metrics/10c3e51a-10e6-419e-8570-97a5e2e418f7                              3     0(0.00%) |     10       8      12     11 |    0.00        0.00
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              6     0(0.00%) |     13      10      19     12 |    0.20        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              2    1(50.00%) |     19      15      24     15 |    0.00        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              5    1(20.00%) |     23       8      74     11 |    0.10        0.00
GET      /v1/quiz/metrics/6a2d92f5-2099-47d8-b962-0b222d649a4b                              3     0(0.00%) |     13      10      15     15 |    0.10        0.00
GET      /v1/quiz/metrics/7252045d-4936-45a3-b06a-71ef15fdde83                              1     0(0.00%) |      8       8       8      8 |    0.00        0.00
GET      /v1/quiz/metrics/72aa43fb-feef-48bb-a87f-bb964858454c                              2     0(0.00%) |      8       5      12      5 |    0.00        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              2     0(0.00%) |     10       7      12      7 |    0.00        0.00
GET      /v1/quiz/metrics/95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                              3     0(0.00%) |     77       6     210     15 |    0.00        0.00
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              2     0(0.00%) |     16      14      18     15 |    0.00        0.00
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                              1     0(0.00%) |     15      15      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/bfe4a522-1c93-40fd-bb19-aba9aca034fd                              3     0(0.00%) |     15       6      32      8 |    0.00        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              2     0(0.00%) |     11      10      12     10 |    0.00        0.00
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              3     0(0.00%) |     13      11      15     13 |    0.10        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/eecb7e1c-adee-4807-8da7-d9a03326cc13                              1     0(0.00%) |     18      18      18     18 |    0.00        0.00
GET      /v1/quiz/metrics/f45f9a26-8ac6-4fe1-83b1-98538770e29c                              4     0(0.00%) |     14      12      16     14 |    0.10        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          9     0(0.00%) |     53      18     244     21 |    0.20        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          7     0(0.00%) |     61      15     242     25 |    0.10        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                         12     0(0.00%) |     18      13      25     19 |    0.20        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          6     0(0.00%) |     28      12      87     19 |    0.10        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          6     0(0.00%) |     21      16      29     21 |    0.10        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          9     0(0.00%) |     28      14      61     23 |    0.20        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          6     0(0.00%) |     33      15     102     19 |    0.20        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          7     0(0.00%) |     16       8      37     14 |    0.00        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          9     0(0.00%) |     24      11      50     21 |    0.30        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                         10     0(0.00%) |     21      15      40     20 |    0.30        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          4     0(0.00%) |     22      14      34     20 |    0.10        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          9     0(0.00%) |     33      14     122     20 |    0.40        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                         10     0(0.00%) |     25      14      90     18 |    0.10        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          7     0(0.00%) |     34      10     123     22 |    0.10        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                         10     0(0.00%) |     23       9      70     17 |    0.20        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                         10     0(0.00%) |     25       7      93     19 |    0.20        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          9     0(0.00%) |     27      13      97     16 |    0.20        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                         10     0(0.00%) |     43      17     168     22 |    0.40        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          7     0(0.00%) |     59      11     244     23 |    0.10        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                          9     0(0.00%) |     34      18     141     22 |    0.20        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       508  113(22.24%) |     21       1     272     16 |   10.40        2.30

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             52     0(0.00%) |     14       2     272      8 |    0.90        0.00
GET      /v1/leaderboard/streak                                                            52     0(0.00%) |      4       1      16      4 |    0.90        0.00
POST     /v1/quiz/answer                                                                  219  116(52.97%) |     19       3     168     17 |    4.20        2.20
GET      /v1/quiz/metrics/10c3e51a-10e6-419e-8570-97a5e2e418f7                              4     0(0.00%) |     11       8      13     11 |    0.00        0.00
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              6     0(0.00%) |     13      10      19     12 |    0.30        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              2    1(50.00%) |     19      15      24     15 |    0.00        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              5    1(20.00%) |     23       8      74     11 |    0.10        0.00
GET      /v1/quiz/metrics/6a2d92f5-2099-47d8-b962-0b222d649a4b                              3     0(0.00%) |     13      10      15     15 |    0.10        0.00
GET      /v1/quiz/metrics/7252045d-4936-45a3-b06a-71ef15fdde83                              1     0(0.00%) |      8       8       8      8 |    0.00        0.00
GET      /v1/quiz/metrics/72aa43fb-feef-48bb-a87f-bb964858454c                              3     0(0.00%) |     11       5      16     12 |    0.00        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              2     0(0.00%) |     10       7      12      7 |    0.10        0.00
GET      /v1/quiz/metrics/95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                              3     0(0.00%) |     77       6     210     15 |    0.00        0.00
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              2     0(0.00%) |     16      14      18     15 |    0.00        0.00
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                              1     0(0.00%) |     15      15      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/bfe4a522-1c93-40fd-bb19-aba9aca034fd                              3     0(0.00%) |     15       6      32      8 |    0.00        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              2     0(0.00%) |     11      10      12     10 |    0.00        0.00
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              3     0(0.00%) |     13      11      15     13 |    0.10        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/eecb7e1c-adee-4807-8da7-d9a03326cc13                              1     0(0.00%) |     18      18      18     18 |    0.00        0.00
GET      /v1/quiz/metrics/f45f9a26-8ac6-4fe1-83b1-98538770e29c                              4     0(0.00%) |     14      12      16     14 |    0.10        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          9     0(0.00%) |     53      18     244     21 |    0.20        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          7     0(0.00%) |     61      15     242     25 |    0.00        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                         13     0(0.00%) |     18      13      25     19 |    0.30        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          7     0(0.00%) |     26      12      87     19 |    0.10        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          6     0(0.00%) |     21      16      29     21 |    0.10        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          9     0(0.00%) |     28      14      61     23 |    0.30        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          6     0(0.00%) |     33      15     102     19 |    0.20        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          7     0(0.00%) |     16       8      37     14 |    0.00        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          9     0(0.00%) |     24      11      50     21 |    0.20        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                         10     0(0.00%) |     21      15      40     20 |    0.30        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          5     0(0.00%) |     22      14      34     20 |    0.10        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          9     0(0.00%) |     33      14     122     20 |    0.40        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                         10     0(0.00%) |     25      14      90     18 |    0.10        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          7     0(0.00%) |     34      10     123     22 |    0.10        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                         10     0(0.00%) |     23       9      70     17 |    0.30        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                         11     0(0.00%) |     24       7      93     19 |    0.30        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                          9     0(0.00%) |     27      13      97     16 |    0.10        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                         10     0(0.00%) |     43      17     168     22 |    0.30        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          7     0(0.00%) |     59      11     244     23 |    0.00        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                          9     0(0.00%) |     34      18     141     22 |    0.20        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       540  118(21.85%) |     21       1     272     16 |   10.40        2.20

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             54     0(0.00%) |     13       2     272      8 |    0.90        0.00
GET      /v1/leaderboard/streak                                                            54     0(0.00%) |      4       1      16      4 |    0.90        0.00
POST     /v1/quiz/answer                                                                  227  119(52.42%) |     19       3     168     17 |    4.00        2.10
GET      /v1/quiz/metrics/10c3e51a-10e6-419e-8570-97a5e2e418f7                              4     0(0.00%) |     11       8      13     11 |    0.10        0.00
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              6     0(0.00%) |     13      10      19     12 |    0.20        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              2    1(50.00%) |     19      15      24     15 |    0.00        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              5    1(20.00%) |     23       8      74     11 |    0.00        0.00
GET      /v1/quiz/metrics/6a2d92f5-2099-47d8-b962-0b222d649a4b                              3     0(0.00%) |     13      10      15     15 |    0.10        0.00
GET      /v1/quiz/metrics/7252045d-4936-45a3-b06a-71ef15fdde83                              1     0(0.00%) |      8       8       8      8 |    0.00        0.00
GET      /v1/quiz/metrics/72aa43fb-feef-48bb-a87f-bb964858454c                              3     0(0.00%) |     11       5      16     12 |    0.10        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              2     0(0.00%) |     10       7      12      7 |    0.10        0.00
GET      /v1/quiz/metrics/95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                              2     0(0.00%) |     12       9      16     10 |    0.00        0.00
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                              3     0(0.00%) |     77       6     210     15 |    0.00        0.00
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              2     0(0.00%) |     16      14      18     15 |    0.00        0.00
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                              1     0(0.00%) |     15      15      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/bfe4a522-1c93-40fd-bb19-aba9aca034fd                              3     0(0.00%) |     15       6      32      8 |    0.00        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              3     0(0.00%) |     12      10      13     13 |    0.00        0.00
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              3     0(0.00%) |     13      11      15     13 |    0.10        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/eecb7e1c-adee-4807-8da7-d9a03326cc13                              1     0(0.00%) |     18      18      18     18 |    0.00        0.00
GET      /v1/quiz/metrics/f45f9a26-8ac6-4fe1-83b1-98538770e29c                              4     0(0.00%) |     14      12      16     14 |    0.10        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          9     0(0.00%) |     53      18     244     21 |    0.20        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          7     0(0.00%) |     61      15     242     25 |    0.00        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                         13     0(0.00%) |     18      13      25     19 |    0.30        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          8     0(0.00%) |     25      12      87     18 |    0.20        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          6     0(0.00%) |     21      16      29     21 |    0.20        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                          9     0(0.00%) |     28      14      61     23 |    0.30        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          6     0(0.00%) |     33      15     102     19 |    0.10        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          7     0(0.00%) |     16       8      37     14 |    0.00        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          9     0(0.00%) |     24      11      50     21 |    0.20        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                         11     0(0.00%) |     21      15      40     20 |    0.20        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          5     0(0.00%) |     22      14      34     20 |    0.20        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          9     0(0.00%) |     33      14     122     20 |    0.40        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                         10     0(0.00%) |     25      14      90     18 |    0.20        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          7     0(0.00%) |     34      10     123     22 |    0.10        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                         11     0(0.00%) |     23       9      70     19 |    0.30        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                         11     0(0.00%) |     24       7      93     19 |    0.30        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                         10     0(0.00%) |     25      13      97     16 |    0.10        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                         11     0(0.00%) |     41      16     168     22 |    0.20        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          8     0(0.00%) |     54      11     244     22 |    0.10        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                         10     0(0.00%) |     32      18     141     21 |    0.20        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       561  121(21.57%) |     21       1     272     16 |   10.40        2.10

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             57     0(0.00%) |     13       2     272      9 |    1.30        0.00
GET      /v1/leaderboard/streak                                                            57     0(0.00%) |      4       1      16      4 |    1.30        0.00
POST     /v1/quiz/answer                                                                  236  123(52.12%) |     19       3     168     17 |    3.90        2.20
GET      /v1/quiz/metrics/10c3e51a-10e6-419e-8570-97a5e2e418f7                              4     0(0.00%) |     11       8      13     11 |    0.10        0.00
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              6     0(0.00%) |     13      10      19     12 |    0.20        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              2    1(50.00%) |     19      15      24     15 |    0.00        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              5    1(20.00%) |     23       8      74     11 |    0.00        0.00
GET      /v1/quiz/metrics/6a2d92f5-2099-47d8-b962-0b222d649a4b                              3     0(0.00%) |     13      10      15     15 |    0.10        0.00
GET      /v1/quiz/metrics/7252045d-4936-45a3-b06a-71ef15fdde83                              1     0(0.00%) |      8       8       8      8 |    0.00        0.00
GET      /v1/quiz/metrics/72aa43fb-feef-48bb-a87f-bb964858454c                              3     0(0.00%) |     11       5      16     12 |    0.10        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              2     0(0.00%) |     10       7      12      7 |    0.10        0.00
GET      /v1/quiz/metrics/95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                              2     0(0.00%) |     12       9      16     10 |    0.00        0.00
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                              3     0(0.00%) |     77       6     210     15 |    0.00        0.00
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              2     0(0.00%) |     16      14      18     15 |    0.00        0.00
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                              1     0(0.00%) |     15      15      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/bfe4a522-1c93-40fd-bb19-aba9aca034fd                              3     0(0.00%) |     15       6      32      8 |    0.00        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              3     0(0.00%) |     12      10      13     13 |    0.10        0.00
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              3     0(0.00%) |     13      11      15     13 |    0.10        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/eecb7e1c-adee-4807-8da7-d9a03326cc13                              1     0(0.00%) |     18      18      18     18 |    0.00        0.00
GET      /v1/quiz/metrics/f45f9a26-8ac6-4fe1-83b1-98538770e29c                              4     0(0.00%) |     14      12      16     14 |    0.10        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          9     0(0.00%) |     53      18     244     21 |    0.20        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          8     0(0.00%) |     56      15     242     23 |    0.00        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                         13     0(0.00%) |     18      13      25     19 |    0.40        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          9     0(0.00%) |     24      12      87     18 |    0.30        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          7     0(0.00%) |     21      16      29     21 |    0.20        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                         10     0(0.00%) |     27      14      61     20 |    0.30        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          7     0(0.00%) |     31      15     102     22 |    0.10        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          7     0(0.00%) |     16       8      37     14 |    0.00        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          9     0(0.00%) |     24      11      50     21 |    0.10        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                         12     0(0.00%) |     21      15      40     20 |    0.20        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          5     0(0.00%) |     22      14      34     20 |    0.10        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          9     0(0.00%) |     33      14     122     20 |    0.30        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                         10     0(0.00%) |     25      14      90     18 |    0.20        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          7     0(0.00%) |     34      10     123     22 |    0.10        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                         11     0(0.00%) |     23       9      70     19 |    0.40        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                         12     0(0.00%) |     23       7      93     18 |    0.20        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                         10     0(0.00%) |     25      13      97     16 |    0.20        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                         12     0(0.00%) |     39      16     168     22 |    0.20        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          8     0(0.00%) |     54      11     244     22 |    0.20        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                         10     0(0.00%) |     32      18     141     21 |    0.10        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       584  125(21.40%) |     20       1     272     16 |   11.20        2.20

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             60     0(0.00%) |     13       2     272      9 |    1.50        0.00
GET      /v1/leaderboard/streak                                                            60     0(0.00%) |      4       1      16      4 |    1.50        0.00
POST     /v1/quiz/answer                                                                  244  126(51.64%) |     19       3     168     17 |    3.70        1.70
GET      /v1/quiz/metrics/10c3e51a-10e6-419e-8570-97a5e2e418f7                              4     0(0.00%) |     11       8      13     11 |    0.10        0.00
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              6     0(0.00%) |     13      10      19     12 |    0.20        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              2    1(50.00%) |     19      15      24     15 |    0.00        0.00
GET      /v1/quiz/metrics/377ac595-5ccf-45c3-8e7f-e61c615c05ea                              1     0(0.00%) |      8       8       8      8 |    0.00        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              5    1(20.00%) |     23       8      74     11 |    0.00        0.00
GET      /v1/quiz/metrics/6a2d92f5-2099-47d8-b962-0b222d649a4b                              3     0(0.00%) |     13      10      15     15 |    0.10        0.00
GET      /v1/quiz/metrics/7252045d-4936-45a3-b06a-71ef15fdde83                              1     0(0.00%) |      8       8       8      8 |    0.00        0.00
GET      /v1/quiz/metrics/72aa43fb-feef-48bb-a87f-bb964858454c                              3     0(0.00%) |     11       5      16     12 |    0.10        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              2     0(0.00%) |     10       7      12      7 |    0.10        0.00
GET      /v1/quiz/metrics/95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                              3     0(0.00%) |     13       9      16     15 |    0.10        0.00
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                              3     0(0.00%) |     77       6     210     15 |    0.00        0.00
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              2     0(0.00%) |     16      14      18     15 |    0.00        0.00
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                              1     0(0.00%) |     15      15      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/bfe4a522-1c93-40fd-bb19-aba9aca034fd                              3     0(0.00%) |     15       6      32      8 |    0.00        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              3     0(0.00%) |     12      10      13     13 |    0.10        0.00
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              3     0(0.00%) |     13      11      15     13 |    0.10        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/eecb7e1c-adee-4807-8da7-d9a03326cc13                              1     0(0.00%) |     18      18      18     18 |    0.00        0.00
GET      /v1/quiz/metrics/f45f9a26-8ac6-4fe1-83b1-98538770e29c                              4     0(0.00%) |     14      12      16     14 |    0.00        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          9     0(0.00%) |     53      18     244     21 |    0.20        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          9     0(0.00%) |     51      11     242     23 |    0.10        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                         13     0(0.00%) |     18      13      25     19 |    0.30        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          9     0(0.00%) |     24      12      87     18 |    0.30        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          7     0(0.00%) |     21      16      29     21 |    0.30        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                         10     0(0.00%) |     27      14      61     20 |    0.20        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          8     0(0.00%) |     30      15     102     21 |    0.10        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          7     0(0.00%) |     16       8      37     14 |    0.00        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                          9     0(0.00%) |     24      11      50     21 |    0.00        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                         12     0(0.00%) |     21      15      40     20 |    0.20        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          5     0(0.00%) |     22      14      34     20 |    0.10        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          9     0(0.00%) |     33      14     122     20 |    0.20        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                         10     0(0.00%) |     25      14      90     18 |    0.10        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          7     0(0.00%) |     34      10     123     22 |    0.10        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                         11     0(0.00%) |     23       9      70     19 |    0.30        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                         12     0(0.00%) |     23       7      93     18 |    0.20        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                         10     0(0.00%) |     25      13      97     16 |    0.10        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                         13     0(0.00%) |     37      16     168     22 |    0.20        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          9     0(0.00%) |     50      11     244     23 |    0.20        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                         10     0(0.00%) |     32      18     141     21 |    0.20        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       604  128(21.19%) |     20       1     272     16 |   11.00        1.70

Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             64     0(0.00%) |     13       2     272      9 |    1.70        0.00
GET      /v1/leaderboard/streak                                                            64     0(0.00%) |      4       1      16      4 |    1.70        0.00
POST     /v1/quiz/answer                                                                  251  131(52.19%) |     19       3     168     17 |    3.80        1.60
GET      /v1/quiz/metrics/10c3e51a-10e6-419e-8570-97a5e2e418f7                              4     0(0.00%) |     11       8      13     11 |    0.10        0.00
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              6     0(0.00%) |     13      10      19     12 |    0.10        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              2    1(50.00%) |     19      15      24     15 |    0.00        0.00
GET      /v1/quiz/metrics/377ac595-5ccf-45c3-8e7f-e61c615c05ea                              1     0(0.00%) |      8       8       8      8 |    0.10        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              5    1(20.00%) |     23       8      74     11 |    0.00        0.00
GET      /v1/quiz/metrics/6a2d92f5-2099-47d8-b962-0b222d649a4b                              3     0(0.00%) |     13      10      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/7252045d-4936-45a3-b06a-71ef15fdde83                              2     0(0.00%) |      9       8       9      8 |    0.00        0.00
GET      /v1/quiz/metrics/72aa43fb-feef-48bb-a87f-bb964858454c                              3     0(0.00%) |     11       5      16     12 |    0.10        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              2     0(0.00%) |     10       7      12      7 |    0.10        0.00
GET      /v1/quiz/metrics/95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                              3     0(0.00%) |     13       9      16     15 |    0.10        0.00
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                              3     0(0.00%) |     77       6     210     15 |    0.00        0.00
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              2     0(0.00%) |     16      14      18     15 |    0.00        0.00
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                              1     0(0.00%) |     15      15      15     15 |    0.00        0.00
GET      /v1/quiz/metrics/bfe4a522-1c93-40fd-bb19-aba9aca034fd                              3     0(0.00%) |     15       6      32      8 |    0.00        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              3     0(0.00%) |     12      10      13     13 |    0.10        0.00
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              3     0(0.00%) |     13      11      15     13 |    0.00        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.00        0.00
GET      /v1/quiz/metrics/eecb7e1c-adee-4807-8da7-d9a03326cc13                              1     0(0.00%) |     18      18      18     18 |    0.00        0.00
GET      /v1/quiz/metrics/f45f9a26-8ac6-4fe1-83b1-98538770e29c                              4     0(0.00%) |     14      12      16     14 |    0.00        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                          9     0(0.00%) |     53      18     244     21 |    0.10        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                          9     0(0.00%) |     51      11     242     23 |    0.10        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                         13     0(0.00%) |     18      13      25     19 |    0.20        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          9     0(0.00%) |     24      12      87     18 |    0.30        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          7     0(0.00%) |     21      16      29     21 |    0.20        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                         10     0(0.00%) |     27      14      61     20 |    0.20        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          8     0(0.00%) |     30      15     102     21 |    0.20        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          8     0(0.00%) |     17       8      37     14 |    0.00        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                         10     0(0.00%) |     24      11      50     20 |    0.00        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                         12     0(0.00%) |     21      15      40     20 |    0.20        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          6     0(0.00%) |     21      14      34     20 |    0.10        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                          9     0(0.00%) |     33      14     122     20 |    0.10        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                         11     0(0.00%) |     25      14      90     18 |    0.10        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          7     0(0.00%) |     34      10     123     22 |    0.10        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                         11     0(0.00%) |     23       9      70     19 |    0.20        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                         12     0(0.00%) |     23       7      93     18 |    0.30        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                         10     0(0.00%) |     25      13      97     16 |    0.10        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                         13     0(0.00%) |     37      16     168     22 |    0.30        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          9     0(0.00%) |     50      11     244     23 |    0.30        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                         11     0(0.00%) |     31      18     141     21 |    0.20        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       625  133(21.28%) |     20       1     272     16 |   11.20        1.60

[2026-02-07 16:35:09,118] Parimals-MacBook-Air/INFO/locust.main: --run-time limit reached, shutting down
[2026-02-07 16:35:09,172] Parimals-MacBook-Air/INFO/locust.main: Shutting down (exit code 1)
Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /v1/leaderboard/score                                                             67     0(0.00%) |     12       2     272      9 |    1.12        0.00
GET      /v1/leaderboard/streak                                                            67     0(0.00%) |      4       1      16      4 |    1.12        0.00
POST     /v1/quiz/answer                                                                  258  136(52.71%) |     19       3     168     17 |    4.32        2.28
GET      /v1/quiz/metrics/10c3e51a-10e6-419e-8570-97a5e2e418f7                              4     0(0.00%) |     11       8      13     11 |    0.07        0.00
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                              6     0(0.00%) |     13      10      19     12 |    0.10        0.00
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                              2    1(50.00%) |     19      15      24     15 |    0.03        0.02
GET      /v1/quiz/metrics/377ac595-5ccf-45c3-8e7f-e61c615c05ea                              1     0(0.00%) |      8       8       8      8 |    0.02        0.00
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                              5    1(20.00%) |     23       8      74     11 |    0.08        0.02
GET      /v1/quiz/metrics/6a2d92f5-2099-47d8-b962-0b222d649a4b                              3     0(0.00%) |     13      10      15     15 |    0.05        0.00
GET      /v1/quiz/metrics/7252045d-4936-45a3-b06a-71ef15fdde83                              2     0(0.00%) |      9       8       9      8 |    0.03        0.00
GET      /v1/quiz/metrics/72aa43fb-feef-48bb-a87f-bb964858454c                              3     0(0.00%) |     11       5      16     12 |    0.05        0.00
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              2     0(0.00%) |     10       7      12      7 |    0.03        0.00
GET      /v1/quiz/metrics/95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                              3     0(0.00%) |     13       9      16     15 |    0.05        0.00
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                              3     0(0.00%) |     77       6     210     15 |    0.05        0.00
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              2     0(0.00%) |     16      14      18     15 |    0.03        0.00
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                              1     0(0.00%) |     15      15      15     15 |    0.02        0.00
GET      /v1/quiz/metrics/bfe4a522-1c93-40fd-bb19-aba9aca034fd                              3     0(0.00%) |     15       6      32      8 |    0.05        0.00
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                              3     0(0.00%) |     12      10      13     13 |    0.05        0.00
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              3     0(0.00%) |     13      11      15     13 |    0.05        0.00
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                              1     0(0.00%) |     16      16      16     16 |    0.02        0.00
GET      /v1/quiz/metrics/eecb7e1c-adee-4807-8da7-d9a03326cc13                              1     0(0.00%) |     18      18      18     18 |    0.02        0.00
GET      /v1/quiz/metrics/f45f9a26-8ac6-4fe1-83b1-98538770e29c                              4     0(0.00%) |     14      12      16     14 |    0.07        0.00
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                         10     0(0.00%) |     50      18     244     21 |    0.17        0.00
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                         10     0(0.00%) |     49      11     242     23 |    0.17        0.00
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                         14     0(0.00%) |     18      13      25     18 |    0.23        0.00
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                          9     0(0.00%) |     24      12      87     18 |    0.15        0.00
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                          7     0(0.00%) |     21      16      29     21 |    0.12        0.00
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                         10     0(0.00%) |     27      14      61     20 |    0.17        0.00
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                          8     0(0.00%) |     30      15     102     21 |    0.13        0.00
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                          8     0(0.00%) |     17       8      37     14 |    0.13        0.00
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                         11     0(0.00%) |     23      11      50     20 |    0.18        0.00
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                         12     0(0.00%) |     21      15      40     20 |    0.20        0.00
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                          7     0(0.00%) |     20      14      34     20 |    0.12        0.00
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                         10     0(0.00%) |     32      14     122     20 |    0.17        0.00
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                         11     0(0.00%) |     25      14      90     18 |    0.18        0.00
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                          7     0(0.00%) |     34      10     123     22 |    0.12        0.00
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                         11     0(0.00%) |     23       9      70     19 |    0.18        0.00
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                         13     0(0.00%) |     23       7      93     18 |    0.22        0.00
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                         10     0(0.00%) |     25      13      97     16 |    0.17        0.00
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                         13     0(0.00%) |     37      16     168     22 |    0.22        0.00
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                          9     0(0.00%) |     50      11     244     23 |    0.15        0.00
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                         12     0(0.00%) |     31      18     141     21 |    0.20        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                       646  138(21.36%) |     20       1     272     16 |   10.82        2.31

Response time percentiles (approximated)
Type     Name                                                                                  50%    66%    75%    80%    90%    95%    98%    99%  99.9% 99.99%   100% # reqs
--------|--------------------------------------------------------------------------------|--------|------|------|------|------|------|------|------|------|------|------|------
GET      /v1/leaderboard/score                                                                   9     10     11     12     13     18     29    270    270    270    270     67
GET      /v1/leaderboard/streak                                                                  4      5      6      6      7      7     10     16     16     16     16     67
POST     /v1/quiz/answer                                                                        17     21     22     23     26     32     45     90    170    170    170    258
GET      /v1/quiz/metrics/10c3e51a-10e6-419e-8570-97a5e2e418f7                                  13     13     13     13     13     13     13     13     13     13     13      4
GET      /v1/quiz/metrics/17ff831a-79f4-4c4a-b35e-5805cd343ad1                                  13     13     16     16     19     19     19     19     19     19     19      6
GET      /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e                                  24     24     24     24     24     24     24     24     24     24     24      2
GET      /v1/quiz/metrics/377ac595-5ccf-45c3-8e7f-e61c615c05ea                                   8      8      8      8      8      8      8      8      8      8      8      1
GET      /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e                                  11     13     13     74     74     74     74     74     74     74     74      5
GET      /v1/quiz/metrics/6a2d92f5-2099-47d8-b962-0b222d649a4b                                  15     15     15     15     15     15     15     15     15     15     15      3
GET      /v1/quiz/metrics/7252045d-4936-45a3-b06a-71ef15fdde83                                  10     10     10     10     10     10     10     10     10     10     10      2
GET      /v1/quiz/metrics/72aa43fb-feef-48bb-a87f-bb964858454c                                  12     12     16     16     16     16     16     16     16     16     16      3
GET      /v1/quiz/metrics/81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                                  13     13     13     13     13     13     13     13     13     13     13      2
GET      /v1/quiz/metrics/95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                                  15     15     16     16     16     16     16     16     16     16     16      3
GET      /v1/quiz/metrics/a23039cf-a048-47d5-baa7-3be598ea78a3                                  15     15    210    210    210    210    210    210    210    210    210      3
GET      /v1/quiz/metrics/ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                                  19     19     19     19     19     19     19     19     19     19     19      2
GET      /v1/quiz/metrics/b253074f-8615-445a-83d4-e9b956a77193                                  15     15     15     15     15     15     15     15     15     15     15      1
GET      /v1/quiz/metrics/bfe4a522-1c93-40fd-bb19-aba9aca034fd                                   8      8     33     33     33     33     33     33     33     33     33      3
GET      /v1/quiz/metrics/cc5a65e4-4750-4594-b022-7c20808efe92                                  13     13     14     14     14     14     14     14     14     14     14      3
GET      /v1/quiz/metrics/d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                                  13     13     16     16     16     16     16     16     16     16     16      3
GET      /v1/quiz/metrics/d7cc2ddf-ede6-480a-94a1-f035e946b34d                                  17     17     17     17     17     17     17     17     17     17     17      1
GET      /v1/quiz/metrics/eecb7e1c-adee-4807-8da7-d9a03326cc13                                  18     18     18     18     18     18     18     18     18     18     18      1
GET      /v1/quiz/metrics/f45f9a26-8ac6-4fe1-83b1-98538770e29c                                  14     14     17     17     17     17     17     17     17     17     17      4
GET      /v1/quiz/next?userId=10c3e51a-10e6-419e-8570-97a5e2e418f7                              22     22     23     93    240    240    240    240    240    240    240     10
GET      /v1/quiz/next?userId=17ff831a-79f4-4c4a-b35e-5805cd343ad1                              25     30     31     83    240    240    240    240    240    240    240     10
GET      /v1/quiz/next?userId=1f5057fc-6486-4158-ac97-1c9205cb089e                              19     19     20     22     23     26     26     26     26     26     26     14
GET      /v1/quiz/next?userId=377ac595-5ccf-45c3-8e7f-e61c615c05ea                              18     19     19     21     87     87     87     87     87     87     87      9
GET      /v1/quiz/next?userId=4e999490-25b2-497d-a149-c1e63477c59e                              21     22     23     23     29     29     29     29     29     29     29      7
GET      /v1/quiz/next?userId=641b800a-0b1f-49a7-977a-e3135b971c61                              23     25     31     41     62     62     62     62     62     62     62     10
GET      /v1/quiz/next?userId=6a2d92f5-2099-47d8-b962-0b222d649a4b                              22     22     23     23    100    100    100    100    100    100    100      8
GET      /v1/quiz/next?userId=7252045d-4936-45a3-b06a-71ef15fdde83                              15     20     22     22     37     37     37     37     37     37     37      8
GET      /v1/quiz/next?userId=72aa43fb-feef-48bb-a87f-bb964858454c                              20     21     21     21     39     51     51     51     51     51     51     11
GET      /v1/quiz/next?userId=81a9a23a-17d1-4f5e-bfbd-0a963ae1b34d                              20     21     21     21     22     40     40     40     40     40     40     12
GET      /v1/quiz/next?userId=95b38ecc-ed43-4500-9f7c-3ab8f2177e3f                              20     20     26     26     34     34     34     34     34     34     34      7
GET      /v1/quiz/next?userId=a23039cf-a048-47d5-baa7-3be598ea78a3                              20     21     22     55    120    120    120    120    120    120    120     10
GET      /v1/quiz/next?userId=ad0965f7-bf7c-40b4-a9f7-ad35b1340c5a                              18     20     26     26     28     90     90     90     90     90     90     11
GET      /v1/quiz/next?userId=b253074f-8615-445a-83d4-e9b956a77193                              22     25     28     28    120    120    120    120    120    120    120      7
GET      /v1/quiz/next?userId=bfe4a522-1c93-40fd-bb19-aba9aca034fd                              19     20     20     20     40     71     71     71     71     71     71     11
GET      /v1/quiz/next?userId=cc5a65e4-4750-4594-b022-7c20808efe92                              18     22     23     24     27     93     93     93     93     93     93     13
GET      /v1/quiz/next?userId=d6bf1529-d372-4d01-96b4-ef6c2ae5cbb6                              16     17     22     30     98     98     98     98     98     98     98     10
GET      /v1/quiz/next?userId=d7cc2ddf-ede6-480a-94a1-f035e946b34d                              22     22     22     23     97    170    170    170    170    170    170     13
GET      /v1/quiz/next?userId=eecb7e1c-adee-4807-8da7-d9a03326cc13                              23     23     32     69    240    240    240    240    240    240    240      9
GET      /v1/quiz/next?userId=f45f9a26-8ac6-4fe1-83b1-98538770e29c                              21     22     23     23     24    140    140    140    140    140    140     12
--------|--------------------------------------------------------------------------------|--------|------|------|------|------|------|------|------|------|------|------|------
         Aggregated                                                                             16     19     21     22     26     40     98    170    270    270    270    646

Error report
# occurrences      Error                                                                                               
------------------|---------------------------------------------------------------------------------------------------------------------------------------------
1                  GET /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e: HTTPError('404 Client Error: Not Found for url: /v1/quiz/metrics/4e999490-25b2-497d-a149-c1e63477c59e')
1                  GET /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e: HTTPError('404 Client Error: Not Found for url: /v1/quiz/metrics/1f5057fc-6486-4158-ac97-1c9205cb089e')
136                POST /v1/quiz/answer: HTTPError('400 Client Error: Bad Request for url: /v1/quiz/answer')           
------------------|---------------------------------------------------------------------------------------------------------------------------------------------

