node() {
    git url: "https://github.com/aidanoflann/score_board", credentialsId: 'dc61f703-7780-457a-a44e-9b58dac6aab7'
    sh "git rev-parse HEAD > .git/commit-id"
    def commit_id = readFile('.git/commit-id').trim()
    println commit_id

    stage "docker_login"
    sh "DOCKER_LOGIN_COMMAND=\$(aws ecr get-login)"
    sh "TRIMMED_COMMAND=\$(echo \$DOCKER_LOGIN_COMMAND | tr -d 'https://')"
    sh "\$TRIMMED_COMMAND"

    stage "build"
    sh "docker build . -t score_board"

    stage "publish"
    sh "docker tag score_board:latest 364843010988.dkr.ecr.eu-west-1.amazonaws.com/score_board:latest"
    sh "docker push 364843010988.dkr.ecr.eu-west-1.amazonaws.com/score_board:latest"
}
