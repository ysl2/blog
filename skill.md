# skill

## Skill source

- <https://skills.sh>
- <https://skillhub.tencent.com/>
- <https://clawhub.ai/>

## Add skills

### Add skills from `http://skills.sh`

```bash
# npx skills add vercel-labs/skills -s find-skills -g -y
# npx skills add vercel-labs/agent-browser -s agent-browser -g -y
npx skills add obra/superpowers -g -y
npx skills add othmanadi/planning-with-files -s planning-with-files -g -y
npx skills add anthropics/skills -s pdf -g -y
npx skills add cloudai-x/threejs-skills -g -y
```

### Add skills from source

```bash
mkdir -p ~/.claude/skills
cd ~/.claude
git clone git@github.com:anthropics/skills.git skills-anthropics
cd skills
ln -s ../skills-anthropics/skills/* ./
```
