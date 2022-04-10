import React from 'react';
// import {useParams} from 'react-router-dom'
import {Link} from 'react-router-dom'

const ProjectItem = ({project, deleteProject}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td>{project.name}</td>
            <td>{project.users}</td>
            <td>{project.repo_url}</td>
            <td>
                <button onClick={() => deleteProject(project.id)} type='button'>Delete</button>
            </td>

        </tr>
    )
}
const ProjectsList = ({projects, deleteProject}) => {
    // let {id} = useParams();
    // let filtered_items = projects.filter((project) => project.id === id)
    return (
        <div>
            <table>
                <th>id</th>
                <th>name</th>
                <th>users</th>
                <th>repo_url</th>
                {projects.map((project) => <ProjectItem project={project} deleteProject={deleteProject}/>)}
            </table>
            <Link to='/projects/create'>Create</Link>
        </div>
    )
}
export default ProjectsList