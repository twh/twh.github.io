# waynehendricks.com

Personal site of Wayne Hendricks.

Built with [Hugo](https://gohugo.io/) and the
[Blowfish](https://blowfish.page/) theme.

## Local preview

```sh
git submodule update --init themes/blowfish
hugo server -D
```

## Deploy

GitHub Actions builds and deploys on push to `main`
(see [.github/workflows/deploy.yml](.github/workflows/deploy.yml)).
