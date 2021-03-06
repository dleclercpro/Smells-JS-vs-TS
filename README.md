# On the Impact of Typing on Code Smelliness: An Empirical Comparison Between JavaScript and TypeScript Projects

## Copyright
The code and results found in this repository are the sole work of David Leclerc. Using, copying, or modifying it, either partially or entirely, is not allowed, unless you ask for the owner's explicit permission.

## Instructions
- Rename '.env.orig' to '.env'.
- Define the ROOT_DIR environment variable as the absolute path to the root directory where you cloned an instance of this project.
- Fill in your GitHub and SonarQube credentials in your '.env' file.

## Smell Detector
- SonarQube

## Validity Threats
- Max number of issues that can be fetched from the SonarQube server: 10,000
- Selection of releases only (X.X.X) using tags, manual filtering
- Minimum 25 patch-level releases
- Ignored files with 'test' in their path
- Ignored files which aren't present in all recent releases when computing smell deltas on file scale

## Incompatible JS Projects
- gruntjs/grunt
- strapi/strapi
- meteor/meteor
- nodejs/node
- mrdoob/three.js
- h5bp/html5-boilerplate
- Leaflet/Leaflet
- less/less.js
- vuejs/vue
- webpack/webpack
- moment/moment
- trekhleb/javascript-algorithms
- juliangarnier/anime
- adam-p/markdown-here
- parcel-bundler/parcel
- TryGhost/Ghost
- mozilla/pdf.js
- impress/impress.js
- facebook/react
- facebook/react-native
- microsoft/playwright
- vuejs/vue
- twbs/bootstrap
- atom/atom
- FortAwesome/Font-Awesome
- hakimel/reveal.js
- mui-org/material-ui
- lodash/lodash
- prettier/prettier
- gatsbyjs/gatsby
- algorithm-visualizer/algorithm-visualizer
- cypress-io/cypress
- Marak/faker.js
- adobe/brackets
- videojs/video.js
- gulpjs/gulp
- RocketChat/Rocket.Chat
- photonstorm/phaser
- agalwood/Motrix
- vuejs/vue-cli
- SheetJS/sheetjs
- jgraph/drawio
- gorhill/uBlock
- Unitech/pm2

## Incompatible TS Projects
- facebook/jest
- ant-design/ant-design
- angular/angular
- cheeriojs/cheerio
- typeorm/typeorm
- fingerprintjs/fingerprintjs
- microsoft/vscode
- neoclide/coc.nvim
- reduxjs/react-redux
- reduxjs/redux-thunk
- vercel/next.js
- GeekyAnts/NativeBase
- redis/node-redis
- n8n-io/n8n
- reduxjs/redux
- ReactiveX/rxjs
- sass/sass
- NativeScript/NativeScript
- nestjs/nest
- puppeteer/puppeteer
- sveltejs/svelte
- babel/babel
- signalapp/Signal-Desktop
- wechaty/wechaty
- storybookjs/storybook
- apollographql/apollo-server
- tensorflow/tfjs
- fullcalendar/fullcalendar
- BabylonJS/Babylon.js
- cdr/code-server
- coder/code-server
- date-fns/date-fns
- apache/superset
- pixijs/pixijs
- vitejs/vite
- vuetifyjs/vuetify
- immutable-js/immutable-js
- apache/echarts
- postcss/postcss
- laurent22/joplin
- angular/angular-cli
- niklasvh/html2canvas
- mobxjs/mobx
- supabase/supabase
- chakra-ui/chakra-ui
- angular/components
- doczjs/docz
- t4t5/sweetalert
- vuejs/devtools
- ianstormtaylor/slate
- Eugeny/tabby
- prisma/prisma
- elastic/kibana
- GoogleChromeLabs/squoosh
- recharts/recharts
- jquense/yup
- grafana/grafana
- excalidraw/excalidraw
- conwnet/github1s
- codex-team/editor.js
- notable/notable
- lensapp/lens