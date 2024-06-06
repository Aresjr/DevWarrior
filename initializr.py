from database import db
from models.skills import Skill, SkillCategory
from models.user import Class, Title

def create_skills():
    coding = SkillCategory(name='Coding')
    database = SkillCategory(name='Database')
    data_science = SkillCategory(name='Data Science & Big Data')
    testing = SkillCategory(name='Testing')
    framework = SkillCategory(name='Framework')
    cloud = SkillCategory(name='Cloud')
    dev_ops = SkillCategory(name='DevOps')

    java = Skill(name='Java', category=coding)
    python = Skill(name='Python', category=coding)
    javascript = Skill(name='Javascript', category=coding)
    typescript = Skill(name='Typescript', category=coding)
    csharp = Skill(name='C#', category=coding)
    ruby = Skill(name='Ruby', category=coding)
    go = Skill(name='Go', category=coding)
    swift = Skill(name='Swift', category=coding)
    kotlin = Skill(name='Kotlin', category=coding)
    scala = Skill(name='Scala', category=coding)
    dart = Skill(name='Dart', category=coding)
    php = Skill(name='PHP', category=coding)
    rust = Skill(name='Rust', category=coding)
    sql = Skill(name='SQL', category=coding)

    mysql = Skill(name='MySQL', category=database)
    oracle = Skill(name='Oracle', category=database)
    mongodb = Skill(name='MongoDB', category=database)
    postgresql = Skill(name='PostgreSQL', category=database)
    redis = Skill(name='Redis', category=database)

    junit = Skill(name='JUnit', category=testing)
    cucumber = Skill(name='Cucumber', category=testing)
    selenium = Skill(name='Selenium', category=testing)
    cypress = Skill(name='Cypress', category=testing)
    unit_test = Skill(name='Unit Test', category=testing)
    component_test = Skill(name='Component Test', category=testing)
    integration_test = Skill(name='Integration Test', category=testing)

    flask = Skill(name='Flask', category=framework)
    spring = Skill(name='Spring', category=framework)
    spring_boot = Skill(name='Spring Boot', category=framework)
    spring_mvc = Skill(name='Spring MVC', category=framework)
    angular = Skill(name='Angular', category=framework)
    react = Skill(name='React', category=framework)
    nodejs = Skill(name='Node.js', category=framework)
    flutter = Skill(name='Flutter', category=framework)
    django = Skill(name='Django', category=framework)
    fastapi = Skill(name='FastAPI', category=framework)
    android = Skill(name='Android', category=framework)
    ios = Skill(name='iOS', category=framework)
    dotnet = Skill(name='.NET', category=framework)

    pandas = Skill(name='Pandas', category=data_science)
    numpy = Skill(name='Numpy', category=data_science)
    scikit_learn = Skill(name='Scikit-Learn', category=data_science)
    tensorflow = Skill(name='TensorFlow', category=data_science)
    spark = Skill(name='Spark', category=data_science)
    jupyter = Skill(name='Jupyter', category=data_science)

    aws = Skill(name='AWS', category=cloud)
    azure = Skill(name='Azure', category=cloud)
    gcp = Skill(name='GCP', category=cloud)
    google_cloud = Skill(name='Google Cloud', category=cloud)

    docker = Skill(name='Docker', category=dev_ops)
    kubernetes = Skill(name='Kubernetes', category=dev_ops)
    aws_ecs = Skill(name='AWS ECS', category=dev_ops)
    aws_lambda = Skill(name='AWS Lambda', category=dev_ops)
    aws_s3 = Skill(name='AWS S3', category=dev_ops)
    aws_sqs = Skill(name='AWS SQS', category=dev_ops)
    aws_sns = Skill(name='AWS SNS', category=dev_ops)
    aws_ses = Skill(name='AWS SES', category=dev_ops)
    aws_dynamodb = Skill(name='AWS DynamoDB', category=dev_ops)
    ci_cd = Skill(name='CI/CD', category=dev_ops)

    db.session.add_all([
        java, python, javascript, typescript, csharp, ruby, go, swift, kotlin, scala, dart, php, rust, sql,
        mysql, oracle, mongodb, postgresql, redis, junit, cucumber, selenium, cypress, unit_test, component_test,
        integration_test, flask, spring, spring_boot, spring_mvc, angular, react, nodejs, flutter, django, fastapi,
        android, ios, dotnet, pandas, numpy, scikit_learn, tensorflow, spark, jupyter, aws, azure, gcp, google_cloud,
        docker, kubernetes, aws_ecs, aws_lambda, aws_s3, aws_sqs, aws_sns, aws_ses, aws_dynamodb, ci_cd
    ])
    db.session.commit()

def create_classes():
    warrior = Class(name='Warrior')
    fighter = Class(name='Fighter')
    paladin = Class(name='Paladin')
    wizard = Class(name='Wizard')
    mage = Class(name='Mage')
    archer = Class(name='Archer')
    druid = Class(name='Druid')
    barbarian = Class(name='Barbarian')
    berserker = Class(name='Berserker')
    rogue = Class(name='Rogue')
    cleric = Class(name='Cleric')
    ranger = Class(name='Ranger')
    bard = Class(name='Bard')
    monk = Class(name='Monk')
    knight = Class(name='Knight')
    alchemist = Class(name='Alchemist')
    healer = Class(name='Healer')
    sorcerer = Class(name='Sorcerer')
    necromancer = Class(name='Necromancer')
    gunfighter = Class(name='Gunfighter')
    hunter = Class(name='Hunter')
    db.session.add_all([
        warrior, fighter, paladin, wizard, mage, archer, druid, barbarian, berserker, rogue, cleric, ranger, bard, monk,
        knight, alchemist, healer, sorcerer, necromancer, gunfighter, hunter
    ])
    db.session.commit()

def create_titles():
    backend_engineer = Title(name='Backend Engineer')
    frontend_engineer = Title(name='Frontend Engineer')
    fullstack_engineer = Title(name='Fullstack Engineer')
    tester = Title(name='Tester')
    qa = Title(name='QA')
    software_architect = Title(name='Software Architect')
    software_engineer = Title(name='Software Engineer')
    tech_lead = Title(name='Tech Lead')

    db.session.add_all([backend_engineer, frontend_engineer, fullstack_engineer, tester, qa, software_architect,
                        software_engineer, tech_lead])
    db.session.commit()

def initialize():
    create_skills()
    create_classes()
    create_titles()
