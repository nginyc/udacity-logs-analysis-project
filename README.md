# Logs Analysis Udacity Project

This project generates a report of a mock PostgreSQL database for a fictional news website using Python. The report answers the following questions:

1. What are the most popular three articles of all time?

2. Who are the most popular article authors of all time?

3. On which days did more than 1% of requests lead to errors?

## Installation

1. Install the appropriate version of [VirtualBox 5.1](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) for your operating system.

2. Install the appropriate version of [Vagrant](https://www.vagrantup.com/downloads.html) for your operating system.

> On Windows, you may need to grant network permissions to Vagrant or make a firewall exception.

3. Download and unzip the [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip).

4. Download and unzip [`newsdata.zip`](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Move the resultant `newsdata.sql` file into `FSND-Virtual-Machine/vagrant/newsdata.sql`. The SQL file contains the SQL commands to fully construct the `news` PostgreSQL database.

5. Using a terminal, change to the directory of `FSND-Virtual-Machine/vagrant` folder with the `cd` command, then start the virtual machine with the command `vagrant up`. Vagrant will download the Linux operating system and install it, together with the dependencies & libraries configured for the virtual machine environment, including PostgreSQL & Python.

> On Windows, [Git Bash](https://git-scm.com/downloads) is recommended.

6. After getting the shell prompt back, run `vagrant ssh`. `cd` into `/vagrant`.

7. Construct the `news` database by running:

```shell
psql -d news -f newsdata.sql
```

8. Clone this repository into `/vagrant`. `cd` into the project directory.

9. Initialize the required PostgreSQL views by running:

```shell
psql -d news -f create_views.sql
```

## Running the Program

Generate the logs analysis report by running:

```shell
./report.py
```

The Python script connects to the `news` PostgreSQL database and leverages on SQL and the views created by `create_views.py` to extract the necessary data for the report.

> The Python script uses `psycopg2` Python module, which should have been pre-installed in the virtual machine.