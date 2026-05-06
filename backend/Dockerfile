FROM maven:3.9.8-jdk-17-slim
WORKDIR /app
COPY .mvn .mvn
COPY mvnw .
COPY pom.xml .
COPY src ./src
RUN chmod +x ./mvnw && ./mvnw -q -DskipTests package
EXPOSE 8080
CMD ["java", "-jar", "target/tool-0.0.1-SNAPSHOT.jar"]
