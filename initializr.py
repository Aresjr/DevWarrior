from models import db, SkillCategory, Skill, Class


def create_skills():
    coding = SkillCategory(name='Coding')
    database = SkillCategory(name='Database')
    data_science = SkillCategory(name='Data Science')
    testing = SkillCategory(name='Testing')
    framework = SkillCategory(name='Framework')
    cloud = SkillCategory(name='Cloud')

    db.session.add_all([coding, database, data_science, testing, framework])
    db.session.commit()

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

    aws = Skill(name='AWS', category=cloud)
    azure = Skill(name='Azure', category=cloud)
    gcp = Skill(name='GCP', category=cloud)

    db.session.add_all([
        java, python, javascript, typescript, csharp, ruby, go, swift, kotlin, scala, dart, php, rust, sql,
        mysql, oracle, mongodb, postgresql, redis, junit, cucumber, selenium, cypress,
        flask, spring, spring_boot, spring_mvc, angular, react, nodejs, flutter, django, fastapi, android, ios, dotnet,
        pandas, numpy, scikit_learn, tensorflow, aws, azure, gcp
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


def initialize():
    create_skills()
    create_classes()
