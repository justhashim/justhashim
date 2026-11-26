<a href="https://hashimweb.netlify.app">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/justhashim/justhashim/main/assets/banner-lockin.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/justhashim/justhashim/main/assets/banner-play.svg">
    <img alt="Hashim Mohamed. I build stuff, mostly for fun. And sometimes I lock in." src="https://raw.githubusercontent.com/justhashim/justhashim/main/assets/banner-play.svg" width="100%">
  </picture>
</a>

<p align="center">
  <samp>
    <a href="https://hashimweb.netlify.app">portfolio</a> .
    <a href="https://hashimmohamedta.medium.com/">medium</a> .
    <a href="https://www.linkedin.com/in/hashimmohamedta/">linkedin</a> .
    <a href="https://www.instagram.com/ha._shim_/">instagram</a> .
    <a href="https://hashimweb.netlify.app/Hashim%20Mohamed%20T.A%20-%20Resume.pdf">résumé</a>
  </samp>
  <br>
  <sub>Light theme is play mode. Switch GitHub to dark to lock in.</sub>
</p>

I goof off 90% of the time and lock in for the 10% that matters.

Most of this account is the 90%. A horror game in an abandoned asylum. Cards for friends. An alarm clock that backs away when you get within 20 cm.

The 10% is backend work. Java and Spring Boot as an intern at Linsys Innovations. Node, Fastify or Python when the project wants it. Postgres under almost all of it.

I'm doing a B.Tech in Computer Science at Model Engineering College, Thrikkakara. Class of '28.

Do I always know what I'm doing? Not really.

Hasn't stopped me yet.

## The 10%

The ones I was locked in for.

- **[rolecall](https://github.com/justhashim/rolecall)**. A job-matching agent over a live jobs index. Hybrid search on Postgres and pgvector, and evals that measure search quality instead of eyeballing it. The model isn't allowed to recommend a job it never retrieved. If it tries, the answer gets rejected and sent back to be fixed.
- **[BrightLoop](https://github.com/justhashim/BrightLoop)**. Subscription billing that refuses to charge anyone twice. A unique index on `(subscription_id, period_index)` turns double-billing into a constraint violation. Run billing again and the duplicates just bounce.
- **[STVE](https://github.com/justhashim/STVE)**. A trust layer for IoT soil sensors. Every reading gets scored as `0.3 temporal + 0.5 cross + 0.2 physical`. One probe drifting on its own is a broken sensor, and it gets a ticket. The whole zone moving together is a `FIELD_EVENT`. That one's real.
- **[Tetherverse](https://github.com/justhashim/Tetherverse-Frontend)**. A swing-and-climb physics game. Hold to grapple, release to launch. Score runs are managed by the server, because the client can't be trusted. [Play it](https://tetherverse.vercel.app).
- **[StoryWeave](https://github.com/justhashim/StoryWeave)**. Collaborative storytelling over WebSockets. People add lines. Every fifth one, GPT-2 throws in a plot twist. It won Grab A Pi Hacknight. The prize was a Raspberry Pi 4.

## The 90%

The rest. Mostly for fun. Sometimes for a hackathon.

- **[Shuttumani](https://github.com/justhashim/shuttumani)**: an alarm clock on a scrapped RC car, built at Scraphack. Get within 20 cm and it reverses. Our first hardware project. One wheel is held on with a stick and some glue. [The whole story](https://hashimmohamedta.medium.com/what-happens-when-you-give-beginners-a-pile-of-scraps-and-20-hours-60d4f4abcbbc).
- **[Bridgio](https://github.com/justhashim/bridgio)**: sign language to text and speech, live from a webcam. Won the MecLabs Hackathon.
- **[Shadows of the Abandoned](https://github.com/justhashim/shadows-of-abandoned)**: first-person horror in an abandoned asylum. You get a flashlight. Good luck.
- **[FYV](https://github.com/justhashim/FYV)**: random video chat for college students.
- **[Vestiq](https://github.com/justhashim/Vestiq)**: tag your clothes from photos, then ask an AI stylist what to wear.
- **[Tabletap](https://github.com/justhashim/Tabletap)**: scan the QR on your table and order. Comes with an admin dashboard and a kitchen display that updates live.
- **[treetouch](https://github.com/justhashim/treetouch)**: type an indented outline, get real folders and files. On npm and PyPI, because why pick one.
- **[ktu-exam-predictor](https://github.com/justhashim/ktu-exam-predictor)**: an agent skill that reads past KTU papers and tells you what's likely to come. Exam season makes you build things.
- **[Will-You-Marry-Me](https://github.com/justhashim/Will-You-Marry-Me)**: a proposal page where the No button runs away from your cursor. I might have a thing for stuff that runs away.
- **[CodeCo](https://github.com/justhashim/CodeCo)**: a clingy desktop girlfriend with an affection meter. Satire, I promise.
- **[farewell-card](https://github.com/justhashim/farewell-card)**: a 3D farewell invite. Open the envelope, then spin the card. [Open it](https://farewell-card-seven.vercel.app).

Everything else is in the [repo list](https://github.com/justhashim?tab=repositories).

## Record

| | Hackathon | Year | With |
|---|---|---|---|
| 1st | MecLabs Hackathon | 2025 | [Bridgio](https://github.com/justhashim/bridgio) |
| 2nd | Operation Darknoon, a cybersecurity hackathon | 2025 | |
| 1st | Grab A Pi Hacknight | 2025 | [StoryWeave](https://github.com/justhashim/StoryWeave) |
| Finalist | MecLabs Hackathon | 2024 | [FYV](https://github.com/justhashim/FYV) |
| Finalist | Dr. P. Thevannoor Hackathon | 2022 | [MisFit](https://github.com/justhashim/MisFit) |

Off the hackathon floor: Web Lead at NSDC MEC, Chief System Architect at Spaceborn, Spring Boot intern at Linsys Innovations.

## Lately on Medium

<!-- medium:start -->
- [What Happens When You Give Beginners a Pile of Scraps and 20 Hours?](https://hashimmohamedta.medium.com/what-happens-when-you-give-beginners-a-pile-of-scraps-and-20-hours-60d4f4abcbbc) (Nov 2026)
<!-- medium:end -->

<sub>Updated by a GitHub Action every morning. The long version of everything above lives here.</sub>

## Toolbox

Tools, and where I actually used them.

- **Services**: Java and Spring Boot (Linsys). Node and Express (STVE, Tabletap). Fastify (BrightLoop, Tetherverse). Python (rolecall, StoryWeave, Bridgio). FastAPI (StoryWeave, Bridgio). LLM tool calling (rolecall).
- **Data**: PostgreSQL (rolecall, STVE, BrightLoop, Tetherverse). pgvector and hybrid search (rolecall). Prisma (STVE, Tetherverse). Supabase (StoryWeave, lockin).
- **Interface**: React and Next.js (almost everything). Tailwind. Phaser and Matter.js (Tetherverse). Babylon.js (Shadows of the Abandoned).
- **Delivery**: Docker (rolecall, Tetherverse). Cloudflare Workers (Tetherverse).

Also on the résumé: MySQL, MongoDB, Firebase.

## Say hi

Work, internships, the serious 10%: [LinkedIn](https://www.linkedin.com/in/hashimmohamedta/). The long version: [Medium](https://hashimmohamedta.medium.com/). Everything else: [Instagram](https://www.instagram.com/ha._shim_/).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/justhashim/justhashim/output/github-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/justhashim/justhashim/output/github-snake.svg">
  <img alt="My contribution graph, getting eaten by a snake" src="https://raw.githubusercontent.com/justhashim/justhashim/output/github-snake.svg" width="100%">
</picture>

<details>
<summary>The receipts</summary>
<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats-one-wine-16.vercel.app/api?username=justhashim&show_icons=true&count_private=true&include_all_commits=true&theme=github_dark&bg_color=0d1117&hide_border=true">
  <source media="(prefers-color-scheme: light)" srcset="https://github-readme-stats-one-wine-16.vercel.app/api?username=justhashim&show_icons=true&count_private=true&include_all_commits=true&bg_color=ffffff&hide_border=true">
  <img alt="GitHub stats: commits, stars, pull requests, issues and contributions" src="https://github-readme-stats-one-wine-16.vercel.app/api?username=justhashim&show_icons=true&count_private=true&include_all_commits=true&bg_color=ffffff&hide_border=true">
</picture>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats-one-wine-16.vercel.app/api/top-langs/?username=justhashim&layout=compact&langs_count=8&theme=github_dark&bg_color=0d1117&hide_border=true">
  <source media="(prefers-color-scheme: light)" srcset="https://github-readme-stats-one-wine-16.vercel.app/api/top-langs/?username=justhashim&layout=compact&langs_count=8&bg_color=ffffff&hide_border=true">
  <img alt="Most used languages" src="https://github-readme-stats-one-wine-16.vercel.app/api/top-langs/?username=justhashim&layout=compact&langs_count=8&bg_color=ffffff&hide_border=true">
</picture>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-streak-stats-tan-two-93.vercel.app?user=justhashim&theme=github_dark&background=0d1117&border=0d1117&date_format=j%20M%5B%20Y%5D">
  <source media="(prefers-color-scheme: light)" srcset="https://github-readme-streak-stats-tan-two-93.vercel.app?user=justhashim&background=ffffff&border=ffffff&date_format=j%20M%5B%20Y%5D">
  <img alt="Current and longest contribution streaks" src="https://github-readme-streak-stats-tan-two-93.vercel.app?user=justhashim&background=ffffff&border=ffffff&date_format=j%20M%5B%20Y%5D">
</picture>

</details>
