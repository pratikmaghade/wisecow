# Use the official Ubuntu base image
FROM ubuntu:20.04

# Set non-interactive frontend for apt-get
ENV DEBIAN_FRONTEND=noninteractive

# Install required packages: fortune, cowsay, and netcat-traditional
RUN apt-get update && \
    apt-get install -y fortune cowsay netcat-traditional && \
    apt-get clean

# Copy the wisecow.sh script to /usr/local/bin/
COPY wisecow.sh /usr/local/bin/wisecow.sh

# Convert script line endings to Unix format
RUN apt-get install -y dos2unix && dos2unix /usr/local/bin/wisecow.sh

# Set the script as executable
RUN chmod +x /usr/local/bin/wisecow.sh

# Expose port 4499
EXPOSE 4499

# Run the wisecow.sh script
CMD ["/usr/local/bin/wisecow.sh"]
