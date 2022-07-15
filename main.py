import numpy as np
import matplotlib.pyplot as plt
import matrices


def demographicSimulation(now):
    allAvailableEmployees = 0
    retirementAge = 65

    #TODO If possibleLastgeneration < 1955 check again in which year -> beacuse year of bith 1955 can go in pension with 65
    #TODO ab Jahrgang 1964 gilt Retenaltersgrente von 67
    #TODO Immigration is not part of the calculation
    # TODO mortality is not part of the calculation

    possibleLastGeneration = now - retirementAge

    population = np.concatenate((matrices.history, matrices.future), axis=0)

    workingPopulation = []
    for element in population:
        if element[0] >= possibleLastGeneration:
            workingPopulation.append(element)

    for element in workingPopulation:
        year = element[0]

        if year + 25 <= now:
            employeesInYear = element[1] * 0.9

            allAvailableEmployees += round(employeesInYear)

        elif year + 18 <= now:
            employeesInYear = element[1] * 0.7
            allAvailableEmployees += round(employeesInYear)

        elif (year + 16) == now:
            employeesInYear = element[1] * 0.5
            allAvailableEmployees += round(employeesInYear)

        else:
            allAvailableEmployees += 0

        constantPositiveImmigration = 5.5 * 10 ** 4

        allAvailableEmployees = allAvailableEmployees + constantPositiveImmigration

    return allAvailableEmployees


def start():
    availableEmployeesListWithYears = []
    availableEmployeesListWithoutYears = []

    for element in matrices.years:

        allAvailableEmployees = demographicSimulation(element)
        availableEmployeesListWithYears.append([matrices.years, allAvailableEmployees])
        availableEmployeesListWithoutYears.append(allAvailableEmployees)

        print(f"In {element} there might be number of employees: {allAvailableEmployees}")

    plt.xlim(right=np.max(matrices.years[-1] + 1))  # xmax is your value
    plt.xlim(left=np.min(matrices.years[0] - 1))  # xmin is your value
    plt.ylim(top=np.max(50 * 10 ** 6))  # ymax is your value
    plt.ylim(bottom=np.min(0))  # ymin is your value
    plt.plot(matrices.years, availableEmployeesListWithoutYears)
    plt.scatter(matrices.years, availableEmployeesListWithoutYears)

    plt.plot()

    # avoid autoscaling
    ax = plt.gca()
    ax.get_xaxis().get_major_formatter().set_scientific(False)
    ax.get_yaxis().get_major_formatter().set_scientific(False)
    ax.yaxis.grid(True, which='minor')

    # show grid

    plt.grid(b=None, which='major', axis='both')

    plt.title('Number of Employees in Germany:')
    plt.xlabel('Year')
    plt.ylabel('Employees')
    plt.show()


if __name__ == '__main__':
    start()
